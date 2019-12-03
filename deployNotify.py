# Run using python3 on mac from brew

import requests
import time
from datetime import datetime, timedelta
import json

from playsound import playsound
# import pygame



def gitHubMasterSha(user, repo, gitHubAccessToken = ""):
    URL = f'https://api.github.com/repos/{user}/{repo}/branches/master'

    PARAMS = {'access_token': gitHubAccessToken}
    r = requests.get(url = URL, params = PARAMS)
    if r.status_code != 200:
        raise Exception(f'error connecting to gitHub repo. errCode: {r.status_code}')

    # TO PRETTY PRINT
    # parsed = json.loads(r.text) #as a python object
    # print(json.dumps(parsed, indent=2, sort_keys=True))

    jsonData = r.json()
    commit = jsonData["commit"]

    # print(commit)
    return commit["sha"]

def playSoundPi(soundFile):
    print("PI RING!!!")
    # pygame.mixer.init()
    # pygame.mixer.music.load(soundFile)
    # pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy() == True:
    #     continue

def playSoundMac(soundFile):
    print("MAC RING!!!")
    playsound(soundFile)


# redWingsGoal.mp3 , error.mp3
def sound(soundFile="redWingsGoal.mp3", macMode=True):
    playSoundMac(soundFile) if macMode else playSoundPi(soundFile)



exit = False
checkEvery = 5
githubUser = "microsoft"
githubRepo = "typescript"
gitHubAccessToken = ""

# python doesnt have do-while loops. so lets "prime the pump"
currentSha = gitHubMasterSha(githubUser, githubRepo, gitHubAccessToken)
lastSha = currentSha
# lastSha = "Test start value to always trigger first run"

print("currentSha: ", currentSha)
print("lastSha: ", lastSha)
while not exit:
    time.sleep(checkEvery)
    currentSha = gitHubMasterSha(githubUser, githubRepo)

    print("newSha - lastSha - checked at: ",currentSha, " - ", lastSha, " - ", datetime.now())

    if currentSha != lastSha:
        lastSha = currentSha
        print("BRANCH HAS UPDATED!!!!")
        sound()


