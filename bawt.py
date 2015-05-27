#!/usr/bin/python

import RPi.GPIO as GPIO

import sys
import time
import yaml
import argparse

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

parser = argparse.ArgumentParser(description='Bawt sprinkler controller')

parser.add_argument('--zone', action="store", dest="zone", default=0)
parser.add_argument('--zonefile', action="store", dest="zone_file", default="conf/zones.yaml")
state = parser.add_mutually_exclusive_group(required=True)
state.add_argument('--on', action="store_true", dest="on")
state.add_argument('--off', action="store_true", dest="off")

args = parser.parse_args()

zone_definition = yaml.safe_load(open(args.zone_file))['zones']

for z in zone_definition:
    GPIO.setup(zone_definition[z]['pin'], GPIO.OUT)

zone = zone_definition[int(args.zone)]

if args.on == True:
    GPIO.output(zone['pin'], True)
elif args.off == True:
    GPIO.output(zone['pin'], False)
