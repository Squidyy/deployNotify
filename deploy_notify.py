#!/usr/bin/.env python3

from notify import core, sha, FREQUENCY, REPOS
from twisted.internet import task, reactor

current_shas = dict({})

# init cache dictionary
for repo in REPOS:
    current_shas[repo['repo_name']] = sha.request_latest_sha(repo)

lc = task.LoopingCall(core.check_for_updates, REPOS, current_shas)
lc.start(FREQUENCY)

reactor.run()
