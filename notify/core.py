from notify import sha, sounds
from datetime import datetime


def check_for_updates(repo_configs, current_shas):
    """
    fetch newest commit hash for given repo, check if it matches previous hash

    Parameters
    ----------
    repo_configs : [dict]
        array of JSON objects that contain configuration information for each repository
    current_shas : dict
        contains results of most recent SDH commit checks
    """
    for repo in repo_configs:
        new_sha = sha.request_latest_sha(repo)

        if new_sha != current_shas[repo['repo_name']]:
            print(f"new SHA found for {repo['repo_name']}/{repo['branch']} at {datetime.now()}")
            print('SHA: ' + new_sha)
            sounds.play_sound(repo['sound'])
        else:
            print(f"no changes found for {repo['repo_name']}/{repo['branch']}  at {datetime.now()}")
            print('SHA: ' + current_shas[repo['repo_name']])

        current_shas[repo['repo_name']] = new_sha
