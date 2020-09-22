import RPi.GPIO as GPIO
import time

led=17
pinnr1,pinnr2=27,22
code =[]
geraden=True
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(pinnr1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinnr2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while geraden:
	if GPIO.input(pinnr1):
		print("Button 1 ingedrukt")
		time.sleep(0.5)
		code.append(1)
#		str+="1"
	if GPIO.input(pinnr2):
		print("Button 2 ingedrukt")
		time.sleep(0.5)
		code.append(2)
		#str+="2"
	if len(code) == 4:
		if code == [1,2,2,1]:
			#print("YES")
			GPIO.output(led,True)
			geraden=False
		code=[]
	print(code)
	#elif len(code) > 4:
GPIO.output(led,False)
GPIO.cleanup()
	#	code=[]
