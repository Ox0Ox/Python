import json
import os
import platform

OS_NAME = platform.uname().system
APP_DETAILS_FILE = 'config/applications.json'

with open('C:\HARSH PATNAIK\Python\Friday.TRIAL.1\JARVIS_AI\config\config.json') as file:
    DATA = json.load(file)

if os.path.exists(APP_DETAILS_FILE) is False:
    with open(APP_DETAILS_FILE, 'w') as file:
        file.write('{}')
