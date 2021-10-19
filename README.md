# Sonarqube Exporter created to be used with DefectDojo

I created this code to be used with the [DefectDojo](https://github.com/DefectDojo/django-DefectDojo) Sonarqube import detailed results.

This code uses another python lib [python-sonarqube-api](https://pypi.org/project/python-sonarqube-api/) .

## Usage

`pip install -r requirements.txt`

Get your Sonarcloud tokend and export it on your shell
`export SONARCLOUD_TOKEN=""`

```
➜ python sonarcloud_json.py -h
usage: sonarcloud_json.py [-h] [--severities SEVERITIES] [--types TYPES] [--url URL] [--filename FILENAME]
                          repo

Sonarcloud JSON Exporter v0.1

positional arguments:
  repo                  <organization_repo> can be seen in URL id: https://sonarcloud.io/project/issues?id=

optional arguments:
  -h, --help            show this help message and exit
  --severities SEVERITIES
                        default is all, can be comma separated
  --types TYPES         default is VULNERABILITY only, can be comma separated
  --url URL             default is https://sonarcloud.io
  --filename FILENAME   default is <organization_repo>.json
```

`repo` is the only argument mandatory, by default it will only fetch issue of the type `VULNERABILITY` and from all severities. Default URL used is (https://sonarcloud.io)[https://sonarcloud.io]

This create a json file with all the issues of the target `organization_repo`.