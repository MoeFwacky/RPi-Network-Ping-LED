#!/bin/sh

sudo python ping-server.py > /dev/null 2>&1 &
sudo python ping-client.py > /dev/null 2>&1 &
sudo python ping-controller.py > /dev/null 2>&1 &
