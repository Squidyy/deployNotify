from requests import get
from os import getenv


# build Github request from config object
def request_latest_sha(r_conf):
    github_api = 'https://api.github.com/repos'
    req_url = f"{github_api}/" \
              f"{r_conf['repo_owner']}/" \
              f"{r_conf['repo_name']}/" \
              f"branches/" \
              f"{r_conf['branch']}"
    req_params = {'access_token': getenv('GITHUB_API_TOKEN')}

    res = get(req_url, params=req_params)

    if res.status_code != 200:
        raise Exception(f'Error connecting to gitHub repo. errCode: {res.status_code}')

    return res.json()['commit']['sha']
