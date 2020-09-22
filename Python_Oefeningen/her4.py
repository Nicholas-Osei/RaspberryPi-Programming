import RPi.GPIO as GPIO

pinnr=[27,22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinnr,GPIO.IN)
counter=0
def lol(channel):
	global counter
	if GPIO.event_detected(pinnr[0]):
		counter+=1
	elif GPIO.event_detected(pinnr[1]):
		counter-=1
	print("Er was een interrupt op ",channel," Counter : ",counter)

GPIO.add_event_detect(pinnr[0], GPIO.RISING,callback=lol,bouncetime=300 )
GPIO.add_event_detect(pinnr[1], GPIO.RISING,callback=lol,bouncetime=300 )

while True:
	#if GPIO.event_detected(pinnr[0]):
	#	print("Er was een interrupt")
	pass
