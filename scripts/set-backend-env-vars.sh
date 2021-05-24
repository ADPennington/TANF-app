#!/usr/bin/env bash

CGAPPNAME_BACKEND=$1

# Determine the appropriate BASE_URL for the deployed instance based on the
# provided Cloud.gov App Name
DEFAULT_ROUTE="https://$CGAPPNAME_BACKEND.app.cloud.gov"
if [ -n "$BASE_URL" ]; then
  # Use Shell Parameter Expansion to replace localhost in the URL
  BASE_URL="${BASE_URL//http:\/\/localhost:8080/$DEFAULT_ROUTE}"
else
  BASE_URL="$DEFAULT_ROUTE/v1"
fi

DEFAULT_FRONTEND_ROUTE="${DEFAULT_ROUTE//backend/frontend}"
if [ -n "$FRONTEND_BASE_URL" ]; then
  FRONTEND_BASE_URL="${FRONTEND_BASE_URL//http:\/\/localhost:3000/$DEFAULT_FRONTEND_ROUTE}"
else
  FRONTEND_BASE_URL="$DEFAULT_FRONTEND_ROUTE"
fi

echo "Setting environment variables for $CGAPPNAME_BACKEND"

cf set-env "$CGAPPNAME_BACKEND" ACR_VALUES "$ACR_VALUES"
cf set-env "$CGAPPNAME_BACKEND" BASE_URL "$BASE_URL"
cf set-env "$CGAPPNAME_BACKEND" CLIENT_ASSERTION_TYPE "$CLIENT_ASSERTION_TYPE"
cf set-env "$CGAPPNAME_BACKEND" CLIENT_ID "$CLIENT_ID"
cf set-env "$CGAPPNAME_BACKEND" DJANGO_SECRET_KEY "$DJANGO_SECRET_KEY"
cf set-env "$CGAPPNAME_BACKEND" FRONTEND_BASE_URL "$FRONTEND_BASE_URL"
cf set-env "$CGAPPNAME_BACKEND" OIDC_OP_AUTHORIZATION_ENDPOINT "$OIDC_OP_AUTHORIZATION_ENDPOINT"
cf set-env "$CGAPPNAME_BACKEND" OIDC_OP_ISSUER "$OIDC_OP_ISSUER"
cf set-env "$CGAPPNAME_BACKEND" OIDC_OP_JWKS_ENDPOINT "$OIDC_OP_JWKS_ENDPOINT"
cf set-env "$CGAPPNAME_BACKEND" OIDC_OP_LOGOUT_ENDPOINT "$OIDC_OP_LOGOUT_ENDPOINT"
cf set-env "$CGAPPNAME_BACKEND" OIDC_OP_TOKEN_ENDPOINT "$OIDC_OP_TOKEN_ENDPOINT"
cf set-env "$CGAPPNAME_BACKEND" OIDC_RP_CLIENT_ID "$OIDC_RP_CLIENT_ID"
cf set-env "$CGAPPNAME_BACKEND" PRIVATE_KEY "$PRIVATE_KEY"
cf set-env "$CGAPPNAME_BACKEND" AWS_ACCESS_KEY "$AWS_ACCESS_KEY"
cf set-env "$CGAPPNAME_BACKEND" AWS_SECRET_ACCESS_KEY "$AWS_SECRET_ACCESS_KEY"
cf set-env "$CGAPPNAME_BACKEND" AWS_BUCKET "$AWS_BUCKET"
cf set-env "$CGAPPNAME_BACKEND" AWS_REGION_NAME "$AWS_REGION_NAME"
cf set-env "$CGAPPNAME_BACKEND" AWS_ACCESS_KEY_ID "$AWS_ACCESS_KEY_ID"
cf set-env "$CGAPPNAME_BACKEND" BUCKET_NAME "$BUCKET_NAME"
cf set-env "$CGAPPNAME_BACKEND" DJANGO_AWS_ACCESS_KEY_ID "$DJANGO_AWS_ACCESS_KEY_ID"
cf set-env "$CGAPPNAME_BACKEND" DJANGO_AWS_SECRET_ACCESS_KEY "$DJANGO_AWS_SECRET_ACCESS_KEY"
cf set-env "$CGAPPNAME_BACKEND" DJANGO_AWS_STORAGE_BUCKET_NAME "$DJANGO_AWS_STORAGE_BUCKET_NAME"
cf set-env "$CGAPPNAME_BACKEND" DJANGO_SU_NAME "$DJANGO_SU_NAME"
cf set-env "$CGAPPNAME_BACKEND" DJANGO_CONFIGURATION "$DJANGO_CONFIGURATION"
cf set-env "$CGAPPNAME_BACKEND" DJANGO_SETTINGS_MODULE "$DJANGO_SETTINGS_MODULE"
