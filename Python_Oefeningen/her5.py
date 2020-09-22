import RPi.GPIO as GPIO
import random
import time

led=17
pinnr=[27,22]
counterplayer1=0
counterplayer2=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinnr,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

#GPIO.remove_event_detect(pinnr[0])
#GPIO.remove_event_detect(pinnr[1])

pressed=False
def lol(channel):
	global counterplayer1
	global counterplayer2
	if GPIO.input(led):
		if channel == pinnr[0]:
			counterplayer1+=1
		elif channel == pinnr[1]:
			counterplayer2+=1
		GPIO.output(led,False)
		pressed=True
		print("Player 1: ",counterplayer1," Player 2: ",counterplayer2)

GPIO.add_event_detect(pinnr[0],GPIO.RISING,callback=lol,bouncetime=300)
GPIO.add_event_detect(pinnr[1],GPIO.RISING,callback=lol,bouncetime=300)

while not pressed:
	r = random.randint(1,4)
	time.sleep(r)
	GPIO.output(led,True)
	print("Led On ", r)
	if counterplayer1 >= 10 or counterplayer2 >= 10:
		pressed=True

if counterplayer1 > counterplayer2:
	print("Player 1 wins")
elif counterplayer1 == counterplayer2:
	print("Gelijkspel")
else :
	print("Player 2 wins")
