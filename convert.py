#!/usr/bin/python3

import re
from pathlib import Path
from urllib.request import urlopen

# READ PORT FROM ENV FILE

path = str(Path(__file__).parent.joinpath('.env'))
env = open(path, 'r', encoding='utf-8').read()

matches = re.findall(r"V2RAY_PORT=(\d+)", env)
bridgePort = matches[0]

# FETCH IP ADDRESS

defaultBridgeIP = urlopen('http://ifconfig.io/ip').read().decode().rstrip()
bridgeIP = input(f"Bridge IP: (Leave empty to use `{defaultBridgeIP}`)\n")
if bridgeIP == '':
    bridgeIP = defaultBridgeIP

# INPUT: SS LINK

ssLink = input("Original ss:// link:\n")

matches = re.findall(r"ss://[^@]+@(\d+\.\d+\.\d+\.\d+):(\d+).*", ssLink)
if len(matches[0]) != 2:
    print('Invalid outline (shadowsocks) link.')
    exit(1)

originalIP, originalPort = matches[0]
ssLink = ssLink.replace(originalIP, bridgeIP).replace(originalPort, bridgePort)

# PRINT OUT RESULT

print('New outline link:')
print(ssLink)

print('New invitation link:')
print('https://s3.amazonaws.com/outline-vpn/invite.html#/en/invite/' + ssLink)
