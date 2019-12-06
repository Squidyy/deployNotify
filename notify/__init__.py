import json

with open('config.json') as config_file:
    config = json.load(config_file)

if config is None:
    raise Exception('No `config.json` provided.')

FREQUENCY = config['frequency_seconds']
REPOS = config['repos']
