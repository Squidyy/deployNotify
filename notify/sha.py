from requests import get
from os import getenv


def request_latest_sha(repo_config):
    """
    perform GET request to GitHub API and pull commit SHA hash

    Parameters
    ----------
    repo_config : dict

    Returns
    -------
    str
        commit hash (SHA)
    """
    github_api = 'https://api.github.com/repos'
    req_url = f"{github_api}/" \
              f"{repo_config['repo_owner']}/" \
              f"{repo_config['repo_name']}/" \
              f"branches/" \
              f"{repo_config['branch']}"
    req_params = {'access_token': getenv('GITHUB_API_TOKEN')}

    res = get(req_url, params=req_params)

    if res.status_code != 200:
        raise Exception(f'Error connecting to gitHub repo. errCode: {res.status_code}')

    return res.json()['commit']['sha']
