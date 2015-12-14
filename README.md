# bawt
[![Circle CI](https://circleci.com/gh/DoriftoShoes/bawt/tree/master.svg?style=svg)](https://circleci.com/gh/DoriftoShoes/bawt/tree/master)
## Introduction
bawt is a project aimed at turning a Raspberry Pi into an all in one garage/hydroponic garden controller.

## Setup

To setup create a virtualenv, install the requirements, and run setup.py

```
virtualenv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
python setup.py develop
```

### General Configuration
[main.yaml](conf/main.yaml)
WIP

## Subsystems
### Camera
Control the rPi camera.

#### Configuration
[camera.yaml](conf/camera.yaml)
WIP

### Irrigation
Control relays for irrigation systems

#### Configuration
[irrigation.yaml](conf/irrigation.yaml)
WIP

### Environment
Read environmental sensors

### Configuration
[environment.yaml](conf/environment.yaml)
WIP

## Daemons
### Timelapsed
Timelapsed is used for taking timelapse pictures...surprise, surprise.  It offers a number of configuration options as listed below.

#### Configuration
[camera.yaml](conf/camera.yaml)

Timelapsed is configured through the camera configuration file linked above.  All configuration options are under the `timelapse` section.

|Option|Description|Required|Default|
|:-----:|:--------:|:-----:|:------:|
|enabled|Is timelapse enabled?|NO|true|
|frequency|Picture interval(seconds)|NO|false|
|prefix|Filename prefix|NO|None|
|delete|Delete local file|NO|false|
|hours|Hours of operation|NO|all|

## Tools
### cameratest.py
Can be used for one off captures.
