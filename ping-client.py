#! /usr/bin/python
import os
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

SERVER_BCM =15
CLIENT_BCM =21
CNTRL_BCM =27

#GPIO.setup(SERVER_BCM, GPIO.OUT)
#SERVER_LED = GPIO.PWM( SERVER_BCM, 50)
#SERVER_LED.start(1)
GPIO.setup(CLIENT_BCM, GPIO.OUT)
CLIENT_LED = GPIO.PWM( CLIENT_BCM, 50)
#CLIENT_LED.start(1)
#GPIO.setup(CNTRL_BCM, GPIO.OUT)
#CNTRL_LED = GPIO.PWM( CNTRL_BCM, 50)
#CNTRL_LED.start(1)

server = '192.168.1.101'
client = '192.168.1.102'
controller = '192.168.1.103'
multiplier = 7

#start = time.time()
#action = os.system("ping -c 1 " + server)
#serverping = (time.time() - start) * multiplier

start = time.time()
action = os.system("ping -c 1 " + client)
clientping = (time.time() - start) * multiplier

#start = time.time()
#action = os.system("ping -c 1 " + controller)
#controllerping = (time.time() - start) * multiplier

#def blink_server():
#                time.sleep(serverping)
#                SERVER_LED.start(1)
#                time.sleep(serverping)
#                SERVER_LED.start(0)

def blink_client():
                time.sleep(clientping)
                CLIENT_LED.start(1)
                time.sleep(clientping)
                CLIENT_LED.start(0)

#def blink_controller():
#                time.sleep(controllerping)
#                CNTRL_LED.start(1)
#                time.sleep(controllerping)
#                CNTRL_LED.start(0)

def led():
#                for _ in range(10):
#                        blink_server()
                for _ in range(10):
                        blink_client()
#                for _ in range(10):
#                        blink_controller()
                return

while True:
        led();
        time.sleep(clientping)

#       start = time.time()
#       action = os.system("ping -c 1 " + server)
#       serverping = (time.time() - start) * multiplier

        start = time.time()
        action = os.system("ping -c 1 " + client)
        clientping = (time.time() - start) * multiplier

#       start = time.time()
#       action = os.system("ping -c 1 " + controller)
#       controllerping = (time.time() - start) * multiplier
