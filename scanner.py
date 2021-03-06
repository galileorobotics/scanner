#!/usr/bin/env python
import math
import time
import nxt.locator
from nxt.sensor import *
from nxt.motor import *

ARM_LENGTH = 8.0 # cm
DEG_PER_REAL_DEG = 20 # 500 deg == 25 deg
DEG_PER_CM = 500.0 # 5000 deg == 10 cm

def move(cm):
	speed = -20
	if (cm < 0): speed *= -1
	deg = abs(cm) * DEG_PER_CM
	driving_motor.turn(speed, deg)

def rotate(deg):
	speed = 10
	if (deg < 0): speed *= -1
	deg *= DEG_PER_REAL_DEG
	rotating_motor.turn(speed, abs(deg))

def get_x():
	return math.sin(math.radians(__get_deg())) * ARM_LENGTH

def get_y():
	rot = -driving_motor.get_tacho().rotation_count
	dist = rot / DEG_PER_CM
	dist += math.cos(math.radians(__get_deg())) * ARM_LENGTH
	return dist

def __get_deg():
	return rotating_motor.get_tacho().rotation_count / DEG_PER_REAL_DEG

def get_light():
	return light_sensor.get_sample() / 1000.

brick = nxt.locator.find_one_brick()
light_sensor = Light(brick, PORT_1)
light_sensor.set_illuminated(True)
driving_motor = Motor(brick, PORT_A)
rotating_motor = Motor(brick, PORT_B)