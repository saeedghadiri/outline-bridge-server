#!/usr/bin/python3

import json
import re
from pathlib import Path

# LOAD CONFIG FILES

path = Path(__file__).parent

configPath = str(path.joinpath('config/config.json'))
configFile = open(configPath, 'r', encoding='utf-8')
config = json.load(configFile)

envPath = str(path.joinpath('.env.example'))
envFile = open(envPath, 'r', encoding='utf-8')
env = envFile.read()

# INPUT: SERVER IP

defaultIP = config['inbounds'][0]['settings']['address']
if defaultIP == '<SERVER-IP>':
    message = "Server IP/Hostname:\n"
else:
    message = f"Server IP/Hostname: (Leave empty to use `{defaultIP}`)\n"

serverIP = input(message)
if serverIP == '':
    serverIP = defaultIP

config['inbounds'][0]['settings']['address'] = serverIP

# INPUT: SERVER PORT

defaultPort = config['inbounds'][0]['settings']['port']
serverPort = input(f"Server Port: (Leave empty to use `{defaultPort}`)\n")
if serverPort == '':
    serverPort = defaultPort

config['inbounds'][0]['settings']['port'] = int(serverPort)

# INPUT: BRIDGE PORT

matches = re.findall(r"V2RAY_PORT=(\d+)", env)
defaultBridgePort = matches[0]

bridgePort = input(f"Bridge Port: (Leave empty to use `{defaultBridgePort}`)\n")
if bridgePort == '':
    bridgePort = defaultBridgePort

# SAVE CONFIG FILE

configContent = json.dumps(config, indent=2)
open(configPath, 'w', encoding='utf-8').write(configContent)

# SAVE ENV FILE
envContent = f"V2RAY_PORT={bridgePort}\n"
envPath = str(path.joinpath('.env'))
open(envPath, 'w', encoding='utf-8').write(envContent)

# PRINT OUT RESULT

print('Done!')
