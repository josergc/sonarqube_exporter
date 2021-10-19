#!/usr/bin/python

from sonarqube import SonarCloudClient
import argparse
import os
import sys
import json

__version__="0.1"
__author__="Daniel Loureiro aka dkade - https://github.com/dkade"

if "SONARCLOUD_TOKEN" in os.environ:
    SONARCLOUD_TOKEN=os.environ['SONARCLOUD_TOKEN']
    pass
else:
    print("[ERROR] Missing SONARCLOUD_TOKEN in environment variables.")
    sys.exit(1)

SONAR_URL="https://sonarcloud.io"
SONAR_SEVERITIES="" # empty for all severities, otherwise separate by comma 
SONAR_TYPES="VULNERABILITY" # empty for all types, otherwise separate by comma


parser = argparse.ArgumentParser(description='Sonarcloud JSON Exporter v'+__version__)
parser.add_argument('repo', 
                help='<organization_repo> can be seen in URL id: https://sonarcloud.io/project/issues?id=')
parser.add_argument('--severities', 
                help='default is all, can be comma separated')
parser.add_argument('--types', 
                help='default is VULNERABILITY only, can be comma separated')
parser.add_argument('--url', 
                help='default is https://sonarcloud.io')
parser.add_argument('--filename', 
                help='default is <organization_repo>.json')

args = parser.parse_args()

print("Args: " + str(args))

SONAR_REPO=args.repo
if args.severities != None:
	SONAR_SEVERITIES=args.severities
if args.types != None: 
	SONAR_TYPES=args.types
if args.url != None: 
	SONAR_URL = args.url
if args.filename != None: 
	FILENAME = args.filename
else:
	FILENAME = SONAR_REPO

def create_json(filename, issues_list):
    with open( filename+'.json', 'w') as f:
        json.dump(issues_list, f)

sonar = SonarCloudClient(sonarcloud_url=SONAR_URL, token=SONARCLOUD_TOKEN)
issues = list(sonar.issues.search_issues(componentKeys=SONAR_REPO, severities=SONAR_SEVERITIES, types=SONAR_TYPES, resolved="false"))

create_json(FILENAME,issues)