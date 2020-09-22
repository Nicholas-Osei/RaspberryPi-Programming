import RPi.GPIO as GPIO
import time
import random

pinnen=[5,6,13,19,26,20,21]
display=[18,23,24,25]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinnen,GPIO.OUT)
GPIO.setup(display,GPIO.OUT)
GPIO.output(pinnen,False)
GPIO.output(display,True)
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}


#for p in range(2):
#	GPIO.output(display[p],False)
try:
	while True:
		GPIO.output(display[2],False)
	#for x in range(len(pinnen)):
	#	GPIO.output(pinnen[x],True)
	#	time.sleep(0.5)
	#	GPIO.output(pinnen[x],False)
	#	time.sleep(0.5)
		eh = random.randint(0,9)
		eh+=1
		s=str(eh)
		print(s)
	#for digit in range(4):
		for loop in range(0,7):
			#if len(s)==1:
			GPIO.output(pinnen[loop],num[s[0]][loop])
			#GPIO.output(25, 0)
			#if len(s)==2:
			#	GPIO.output(display[1],False)
#	GPIO.output(display[digit], 0)
		time.sleep(0.5)
#	GPIO.output(display[digit], 1)
except KeyboardInterrupt:
	print("GoodBye! NIGGA")
finally:
	GPIO.cleanup()
