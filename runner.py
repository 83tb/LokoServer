#!/bin/bash
from django.core.management import setup_environ


from django.conf import settings

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LokoServer.settings")

from LokoApp.models import Queue


import serial


serObj = serial.Serial('/dev/tty.usbmodem1411',
                       baudrate=9600,
                       bytesize=serial.EIGHTBITS,
                       parity=serial.PARITY_NONE,
                       stopbits=serial.STOPBITS_ONE,
                       timeout=1,
                       xonxoff=0,
                       rtscts=0
                       )

from time import sleep

while True:


    try:

        command = Queue.objects.filter(done=False)[0]
        serObj.write(command.command + "\n")
        sleep(1)
        command.done = True
        command.save()
    except:
        sleep(5)
        pass


