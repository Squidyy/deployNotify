import json

with open('config.json') as config_file:
    config = json.load(config_file)

FREQUENCY = config['frequency_seconds']
REPOS = config['repos']