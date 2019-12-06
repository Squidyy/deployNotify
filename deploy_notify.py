#!/usr/bin/.env python3

from notify import core, sha, FREQUENCY, REPOS
from twisted.internet import task, reactor
from os import getenv

if getenv('GITHUB_API_TOKEN') is None:
    raise Exception('No Github access token provided.')

current_shas = dict({})

# init cache dictionary
for repo in REPOS:
    current_shas[repo['repo_name']] = sha.request_latest_sha(repo)

print('Deploy Notification polling started.')

lc = task.LoopingCall(core.check_for_updates, REPOS, current_shas)
lc.start(FREQUENCY)

reactor.run()
