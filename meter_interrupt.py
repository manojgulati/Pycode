#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
 
# GPIO 23 set up as input. It is pulled up to stop false signals
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23,GPIO.OUT)
GPIO.output(23, False)
 
 
 
count=0
try:
    while True:
    	GPIO.wait_for_edge(17, GPIO.RISING)
        f=open('/home/pi/Desktop/motor_data.csv','a+')
 
	f.write(str(time.time())+",Rising\n")
	GPIO.wait_for_edge(17, GPIO.FALLING)
	f.write(str(time.time())+",Falling\n")
	
	count+=1
	f.write(str(time.time())+","+str(count)+"\n")
	f.close()
    	
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit