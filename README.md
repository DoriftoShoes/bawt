<p align="center">
<img src="http://hoolboom.com/icons/robot.gif" />
<br />
<a href="https://circleci.com/gh/DoriftoShoes/bawt/tree/master"><img src="https://circleci.com/gh/DoriftoShoes/bawt/tree/master.svg?style=svg" /> </a>
</p>
## Bawt Introduction
Bawt is a project aimed at turning a Raspberry Pi into an all in one garage/hydroponic garden controller.


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

Cross subsystem configurations are done in the main configuration file.

|Option|Description|Required|Default|
|:-----:|:--------:|:-----:|:------:|
|**AWS**||
|access_key|AWS Access Key|YES|None|
|secret_key|AWS Secret Key|YES|None|
|**Logging**||
|config_file|Path to logging config|YES|None|

#### Subsystems
The subsystems configuration is simply to enable or disable the different subsystems.  Available subsystems are:

* [camera](#camera)
* [environment](#environment)
* [irrigation](#irrigation)

Each subsystem will have an `enabled` flag that is either `true` or `false`

## Subsystems
### Camera
Control the rPi camera.

#### Configuration
[camera.yaml](conf/camera.yaml)

|Option|Description|Required|Default|
|:-----:|:--------:|:-----:|:------:|
|directory|Local path to save files|YES|None|
|**remote**||
|type|remote system type|YES|None|
|target|location on remote system|YES|None|
|**resolution**||
|x|horizontal resolution|YES|None|
|y|vertical resolution|YES|None|

### Irrigation
Control relays for irrigation systems

#### Configuration
[irrigation.yaml](conf/irrigation.yaml)

|Option|Description|Required|Default|
|:-----:|:--------:|:-----:|:------:|
|**units**||
|name|user defined name|NO|None|
|pin|GPIO pin|YES|None|
|enabled|Is unit enabled?|NO|true|
|**runs**||
|start_time|Time of day for run|YES|None|
|run_time|Length of run in seconds|YES|None|
|zones|Zones included in run|YES|None|

### Sensor
Read environmental sensors

### Configuration
[sensor.yaml](conf/environment.yaml)

|Option|Description|Required|Default|
|:-----:|:--------:|:-----:|:------:|
|**units**||
|name|user defined long name|NO|None|
|pin|GPIO pin|YES|None|
|enabled|Is sensor enabled?|NO|true|
|type|Sensor model|YES|None|

### Weather
Collect local weather data

#### Configuration
WIP

### HVAC
Control HVAC system

#### Configuration
WIP

### File
Save various data to local or remote systems

#### Configuration
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

### Irrigationd
Irrigationd controls sprinklers and other irrigation systems according to the configuration as defined in irrigation.yaml

#### Configuration
[irrigation.yaml](conf/irrigation.yaml)

Irrigationd is configured through the irrigation configuration file linked above.

## Tools
### cameratest.py
Can be used for one off captures.
