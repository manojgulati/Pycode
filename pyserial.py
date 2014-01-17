import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='com2',
    baudrate=9600)
starttime= 1355735545
while True:
	value= ser.readline()
	#value_list=value.split(",")
	#print value_list[1],value_list[2]
	currenttime=int(time.time())
	if (currenttime-starttime)>180:
		starttime=currenttime
	f=open(str(starttime)+".csv","w")

	line_to_write=str(int(time.time()))+","+value
	
	f.write(line_to_write)
