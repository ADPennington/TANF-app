#!/bin/sh

# The deployment strategy you wish to employ ( rolling update or setting up a new environment)
DEPLOY_STRATEGY=${1}

#The application name  defined via the manifest yml for the frontend
CGAPPNAME_BACKEND=${2}

CF_SPACE=${3}

echo DEPLOY_STRATEGY: "$DEPLOY_STRATEGY"
echo BACKEND_HOST: "$CGAPPNAME_BACKEND"

strip() {
    # Usage: strip "string" "pattern"
    printf '%s\n' "${1##$2}"
}

# The cloud.gov space defined via environment variable (e.g., "tanf-dev", "tanf-staging")
env=$(strip $CF_SPACE "tanf-")

# Determine the appropriate BASE_URL for the deployed instance based on the
# provided Cloud.gov App Name
DEFAULT_ROUTE="https://$CGAPPNAME_BACKEND.app.cloud.gov"
if [ -n "$BASE_URL" ]; then
  # Use Shell Parameter Expansion to replace localhost in the URL
  BASE_URL="${BASE_URL//http:\/\/localhost:8080/$DEFAULT_ROUTE}"
elif [ "$CF_SPACE" = "tanf-prod" ]; then
  # Keep the base url set explicitly for production.
  BASE_URL="$BASE_URL/v1"
else
  # Default to the route formed with the cloud.gov env for the lower environments.
  BASE_URL="$DEFAULT_ROUTE/v1"
fi

DEFAULT_FRONTEND_ROUTE="${DEFAULT_ROUTE//backend/frontend}"
if [ -n "$FRONTEND_BASE_URL" ]; then
  FRONTEND_BASE_URL="${FRONTEND_BASE_URL//http:\/\/localhost:3000/$DEFAULT_FRONTEND_ROUTE}"
elif [ "$CF_SPACE" = "tanf-prod" ]; then
  # Keep the base url set explicitly for production.
  FRONTEND_BASE_URL="$FRONTEND_BASE_URL"
else
  # Default to the route formed with the cloud.gov env for the lower environments.
  FRONTEND_BASE_URL="$DEFAULT_FRONTEND_ROUTE"
fi

# Dynamically generate a new DJANGO_SECRET_KEY
DJANGO_SECRET_KEY=$(python -c "from secrets import token_urlsafe; print(token_urlsafe(50))")

# Dynamically set DJANGO_CONFIGURATION based on Cloud.gov Space
DJANGO_SETTINGS_MODULE="tdpservice.settings.cloudgov"
if [ "$CF_SPACE" = "tanf-prod" ]; then
  DJANGO_CONFIGURATION="Production"
elif [ "$CF_SPACE" = "tanf-staging" ]; then
  DJANGO_CONFIGURATION="Staging"
else
  DJANGO_CONFIGURATION="Development"
fi

set_cf_envs()
{
  cf set-env "$CGAPPNAME_BACKEND" ACR_VALUES "$ACR_VALUES"
  cf set-env "$CGAPPNAME_BACKEND" AMS_CLIENT_ID "$AMS_CLIENT_ID"
  cf set-env "$CGAPPNAME_BACKEND" AMS_CLIENT_SECRET "$AMS_CLIENT_SECRET"
  cf set-env "$CGAPPNAME_BACKEND" AMS_CONFIGURATION_ENDPOINT "$AMS_CONFIGURATION_ENDPOINT"
  cf set-env "$CGAPPNAME_BACKEND" AV_SCAN_URL "$AV_SCAN_URL"
  cf set-env "$CGAPPNAME_BACKEND" BASE_URL "$BASE_URL"
  cf set-env "$CGAPPNAME_BACKEND" CLAMAV_NEEDED "$CLAMAV_NEEDED"
  cf set-env "$CGAPPNAME_BACKEND" DJANGO_CONFIGURATION "$DJANGO_CONFIGURATION"
  cf set-env "$CGAPPNAME_BACKEND" DJANGO_SECRET_KEY "$DJANGO_SECRET_KEY"
  cf set-env "$CGAPPNAME_BACKEND" DJANGO_SETTINGS_MODULE "$DJANGO_SETTINGS_MODULE"
  cf set-env "$CGAPPNAME_BACKEND" DJANGO_SU_NAME "$DJANGO_SU_NAME"
  cf set-env "$CGAPPNAME_BACKEND" FRONTEND_BASE_URL "$FRONTEND_BASE_URL"
  cf set-env "$CGAPPNAME_BACKEND" JWT_KEY "$JWT_KEY"
  cf set-env "$CGAPPNAME_BACKEND" LOGGING_LEVEL "$LOGGING_LEVEL"
}

set_backend_env_vars()
{
  echo "Setting environment variables for $CGAPPNAME_BACKEND"

  # Test to see if the backend app exists yet
  cf set-env "$CGAPPNAME_BACKEND" TEMPORARY_DEPLOYMENT_STATUS_FLAG "true"
  RESULT=$? # Get result of previous command
  if [ $RESULT == 0 ]; then
    set_cf_envs
  else
    echo "Error trying to set environment variables for $CGAPPNAME_BACKEND"
    exit 1
  fi

  cf unset-env "$CGAPPNAME_BACKEND" TEMPORARY_DEPLOYMENT_STATUS_FLAG
  echo "$CGAPPNAME_BACKEND variables loaded"
}


# Helper method to generate JWT cert and keys for new environment
generate_jwt_cert() 
{
    echo "regenerating JWT cert/key"
    yes 'XX' | openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -sha256
    cf set-env "$CGAPPNAME_BACKEND" JWT_CERT "$(cat cert.pem)"
    cf set-env "$CGAPPNAME_BACKEND" JWT_KEY "$(cat key.pem)"
}

update_backend()
{
    cd tdrs-backend || exit
    if [ "$1" = "rolling" ] ; then
        # Do a zero downtime deploy.  This requires enough memory for
        # two apps to exist in the org/space at one time.
        cf push "$CGAPPNAME_BACKEND" --no-route -f manifest.buildpack.yml  --strategy rolling || exit 1
    else
        cf push "$CGAPPNAME_BACKEND" --no-route -f manifest.buildpack.yml
        # set up JWT key if needed
        if cf e "$CGAPPNAME_BACKEND" | grep -q JWT_KEY ; then
            echo jwt cert already created
        else
            generate_jwt_cert
        fi
    fi
    set_backend_env_vars
    cf map-route "$CGAPPNAME_BACKEND" app.cloud.gov --hostname "$CGAPPNAME_BACKEND"
    cd ..
}

bind_backend_to_services() {
    cf bind-service "$CGAPPNAME_BACKEND" "tdp-staticfiles-${env}"
    cf bind-service "$CGAPPNAME_BACKEND" "tdp-datafiles-${env}"
    cf bind-service "$CGAPPNAME_BACKEND" "tdp-db-${env}"

    cf restage "$CGAPPNAME_BACKEND"
}

if [ "$DEPLOY_STRATEGY" = "rolling" ] ; then
    # Perform a rolling update for the backend and frontend deployments if
    # specified, otherwise perform a normal deployment
    update_backend 'rolling'
elif [ "$DEPLOY_STRATEGY" = "bind" ] ; then
    # Bind the services the application depends on and restage the app.
    bind_backend_to_services
elif [ "$DEPLOY_STRATEGY" = "initial" ]; then
    # There is no app with this name, and the services need to be bound to it
    # for it to work. the app will fail to start once, have the services bind,
    # and then get restaged.
    update_backend
    bind_backend_to_services
elif [ "$DEPLOY_STRATEGY" = "rebuild" ]; then
    # You want to redeploy the instance under the same name
    # Delete the existing app (with out deleting the services)
    # and perform the initial deployment strategy.
    cf delete "$CGAPPNAME_BACKEND" -r -f
    update_backend
    bind_backend_to_services
else
    # No changes to deployment config, just deploy the changes and restart
    update_backend
fi
