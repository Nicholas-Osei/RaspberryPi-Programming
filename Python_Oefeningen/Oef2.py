import urllib.request
import RPi.GPIO as GPIO
#webpagina = urllib.request.urlopen('https://darksky.net/forecast/51.2211,4.3997/ca12/nl')
led =17
webpagina = urllib.request.urlopen('https://www.meteo.be/nl/antwerpen')

htmlcode = webpagina.read()

webpagina.close()

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
htmltekst = str(htmlcode)
locate = "Zonnig en droog weer"
pos = htmltekst.find(locate) + len(locate)+8
lol= htmltekst[pos:pos+2]
print(lol)

if lol.isdigit():
	temp=int(lol)
else:
	temp=str(htmltekst[pos:pos+1])
if temp > 10:
	GPIO.output(led,True)
