import RPi.GPIO as GPIO
import time

led=17
pinnr=27
counter=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(pinnr, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	if GPIO.input(pinnr):
	#	print("on")
		time.sleep(0.5)
		counter+=1
	if counter == 1:
		GPIO.output(led,True)
	if counter > 1:
		counter=0
	if counter == 0:
	#	time.sleep(1)
		GPIO.output(led,False)
	#time.sleep(1)
