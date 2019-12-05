from notify import core, FREQUENCY, REPOS
from twisted.internet import task, reactor

current_shas = dict({})

# init cache dictionary
for repo in REPOS:
    current_shas[repo['repo_name']] = ''

#
def run_check():
    core.check_for_updates(REPOS, current_shas)


lc = task.LoopingCall(run_check)
lc.start(FREQUENCY)

reactor.run()
