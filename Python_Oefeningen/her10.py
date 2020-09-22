import RPi.GPIO as GPIO
from time import sleep

led=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)

pwm=GPIO.PWM(led,0)
#for x in range(3):
#	sleep(1)
#	pwm.start(50)

#pwm.ChangeFrequency(0)
