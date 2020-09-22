import RPi.GPIO as GPIO
led=17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
pwmPin=GPIO.PWM(led,1)
pwmPin.start(100)
