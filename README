## Deploy Notify

Python 3 package to play sounds when a new commits 
are added to a branch in a GitHub repository,
e.g merges to a `master` for releases...

It simply polls the GitHub API on a recurring schedule
using the Twisted engine.

### Setup

* `ffplay` is used to play audio files (included with `ffmpeg`)
  * `brew install ffmpeg` - macOS
  * `apt-get install ffmpeg` - Debian
* set environment variable `GITHUB_API_TOKEN` to a valid
token that has access to the desired GitHub repositories
* update repository information in `config.json`
>```json
>{
>  "frequency_seconds": 60,
>  "repos": [
>    {
>      "branch": "master",
>      "repo_name": "upperhand.io",
>      "repo_owner": "upper-hand",
>      "sound": "long_goal.mp3"
>    },
>    {
>      "branch": "master",
>      "repo_name": "fe-upperhand.io",
>      "repo_owner": "upper-hand",
>      "sound": "red_wings_goal.mp3"
>    }
>  ]
>}
>```
