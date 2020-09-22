import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import RPi.GPIO as GPIO

led=17
pinnr=[27,22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinnr,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

def isr(channel):
	if channel==pinnr[0]:
		publish.single("testtopic/lol","UP",hostname="broker.mqttdashboard.com")
	if channel==pinnr[1]:
		publish.single("testtopic/lol","DOWN",hostname="broker.mqttdashboard.com")
GPIO.add_event_detect(pinnr[0],GPIO.RISING,callback=isr,bouncetime=300)
GPIO.add_event_detect(pinnr[1],GPIO.RISING,callback=isr,bouncetime=300)

def on_connect(client, userdata, flags, rc): 
	print("Connected with result code "+str(rc)) 
	client.subscribe("testtopic/lol")
	publish.single("testtopic/lol","hahah",hostname="broker.mqttdashboard.com")
def on_message(client, userdata, msg):
	print(msg.payload)
	if str(msg.payload)=="b'UP'":
		GPIO.output(led,True)
	elif str(msg.payload)=="b'DOWN'":
		GPIO.output(led,False)


client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect("broker.mqttdashboard.com", 1883)
client.loop_forever()

#client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message

#client.connect("broker.mqttdashboard.com", 1883)

