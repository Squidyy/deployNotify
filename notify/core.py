from notify import sha, sounds
from datetime import datetime


def check_for_updates(repos, current_shas):
    for repo in repos:
        new_sha = sha.request_latest_sha(repo)

        if new_sha != current_shas[repo['repo_name']]:
            print(f"new SHA found for {repo['repo_name']}/{repo['branch']} at {datetime.now()}")
            sounds.play_sound(repo['sound'])
        else:
            print(f"no changes to found for {repo['repo_name']}/{repo['branch']}")

        current_shas[repo['repo_name']] = new_sha
