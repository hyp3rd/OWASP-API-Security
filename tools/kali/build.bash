#!/usr/bin/env bash

#######################################
# Determine if a command exists on the system
# Globals:
#   None
# Arguments:
#   A directory or a file
# Returns:
#   0 if the command exists, non-zero on error.
#######################################
__command_exists() {
  command -v "$@" >/dev/null 2>&1
}

#######################################
# Run the build and push docker image
# Globals:
#   None
# Arguments:
#   None
# Returns:
#   None
#######################################
run() {
  if __command_exists uvicorn; then
    docker build -t ghcr.io/hyp3rd/kali-in-docke:v1.0.0 .

    docker push ghcr.io/hyp3rd/kali-in-docker:v1.0.0
  else
    echo "docker is not installed or not running'"
  fi
}

run


