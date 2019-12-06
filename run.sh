#!/usr/bin/.env bash

git clone git@github.com:Squidyy/deployNotify.git .
pip3 install -r requirement.txt
source ./.env

if [[ -z "${GITHUB_API_TOKEN}" ]]; then
  python3 deploy_notifty.py
else
  echo 'Please set GITHUB_API_TOKEN to check repos for changes.'
fi
