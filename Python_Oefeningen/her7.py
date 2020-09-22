from flask import Flask 
import RPi.GPIO as GPIO
app = Flask(__name__)
ledPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin,GPIO.OUT)

n=0
lol =''' <h1 style="color:red;"> Hey Nigga </h1>
<a href="/">Back</a>
<form>	
	<button type "submit" formaction="/click"> Click Me </button>
</form>'''
#<button type "submit" formaction="/pg1/on">ON </button>
@app.route("/")
def hey():
	global n
	n+=1
	x= lol +"Dit is je bezoek nr " +str(n)
	return x
@app.route("/click")
def cli():
	if GPIO.input(ledPin):
		GPIO.output(ledPin,False)
	else:
		GPIO.output(ledPin,True)
	return lol




if __name__ == '__main__': 
	app.run(host="0.0.0.0")
