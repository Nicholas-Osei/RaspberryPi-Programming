import RPi.GPIO as GPIO 
import time 
import random

led=17

pin=[27,22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)
GPIO.setup(led,GPIO.OUT)


player1,player2=0,0
gedrukt=0
go=False
def icb(channel):
	global gedrukt
	global go
	if go:
		if GPIO.event_detected(pin[0]):
			gedrukt=1
		if GPIO.event_detected(pin[1]):
			gedrukt=2	
GPIO.add_event_detect(pin[0], GPIO.RISING,callback=icb, bouncetime=30)
GPIO.add_event_detect(pin[1], GPIO.RISING, callback=icb, bouncetime=30)

while True:
	go=False
	GPIO.output(led,False)
	if not GPIO.input(led):
		x = random.randint(1,4)
		time.sleep(4)
		#print(x)
		GPIO.output(led,True)
		go=True
	while not gedrukt:
		pass
	if gedrukt == 1:
		player1+=1
		GPIO.output(led,False)
		print("Player1: ",player1)
	if gedrukt==2:
		player2+=1
		GPIO.output(led,False)
		print("Player2:",player2)

	gedrukt=0
	print(gedrukt)
