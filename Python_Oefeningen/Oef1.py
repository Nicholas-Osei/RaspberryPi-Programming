import RPi.GPIO as GPIO
import time


led=17
pinnr1=27
pinnr2=22
code=[]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(pinnr1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinnr2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	if GPIO.input(pinnr1):
		time.sleep(0.2)
		print("Button 1 ingedrukt")
		code.append(1)
	if GPIO.input(pinnr2):
		time.sleep(0.2)
		print("Button 2 ingedrukt")
		code.append(2)
	if len(code)>4:
		if code ==[1,2,1,2]:
			GPIO.output(led,True)
			print("HAHAHA")
		code=[]
	print(code)
		#GPIO.output(led, False)
	#time.sleep(0.1)
