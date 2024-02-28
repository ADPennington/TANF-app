#!/bin/bash

# pipefail is needed to correctly carry over the exit code from zap-full-scan.py
set -eo pipefail
set -x

sleep 10
# Construct the project slug from the current branch name and user
PROJECT_SLUG=$CIRCLE_PROJECT_USERNAME/$CIRCLE_PROJECT_REPONAME
echo $PROJECT_SLUG

# These environment variables are exported to Circle CI's BASH_ENV
# by the zap-scanner.sh script for each respective app target.
CMD_ARGS=(
    "$CIRCLE_BUILD_NUM"
    --backend-pass-count ${ZAP_BACKEND_PASS_COUNT:-0}
    --backend-warn-count ${ZAP_BACKEND_WARN_COUNT:-0}
    --backend-fail-count ${ZAP_BACKEND_FAIL_COUNT:-0}
    --frontend-pass-count ${ZAP_FRONTEND_PASS_COUNT:-0}
    --frontend-warn-count ${ZAP_FRONTEND_WARN_COUNT:-0}
    --frontend-fail-count ${ZAP_FRONTEND_FAIL_COUNT:-0}
    --project-slug $PROJECT_SLUG
)
#echo $CMD_ARGS

# Evaluate the full command before passing it in so it doesn't
# get improperly interpolated by Cloud.gov.
#CMD="python manage.py process_owasp_scan ${CMD_ARGS[@]} && echo 'goodbye'"
#echo $CMD

# Submit a CF Task for execution that will run the necessary command
#cf run-task tdp-backend-staging --command "$CMD" --name nightly-owasp-scan

# Format CMD_ARGS into a string to pass to echo and python manage.py
CMD_ARGS_STR="${CMD_ARGS[*]}"
echo "CMD_ARGS: $CMD_ARGS_STR"

# Echo and run the Django management command, displaying its output
echo "Running process_owasp_scan.py with arguments: $CMD_ARGS_STR"
CMD_OUTPUT=$(python manage.py process_owasp_scan ${CMD_ARGS[@]})
echo "$CMD_OUTPUT"

# Proceed with the cf command
FINAL_CMD="python manage.py process_owasp_scan ${CMD_ARGS[@]} && echo 'goodbye'"
echo "Running cf command with FINAL_CMD: $FINAL_CMD"
cf run-task tdp-backend-staging --command "$FINAL_CMD" --name nightly-owasp-scan