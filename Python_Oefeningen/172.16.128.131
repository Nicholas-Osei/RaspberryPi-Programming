import RPi.GPIO as GPIO
import random
from threading import Thread
from flask import Flask
app=Flask(__name__)

pinnen=[27,22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinnen,GPIO.IN)
scroll=0
bevestigd=False
virtuele=[]
gegooid=[]
Menu_Choice=0
def icb(channel):
	global scroll
	if channel == pinnen[0]:
		scroll+=1
		if scroll > 4:
			scroll=1
	elif channel == pinnen[1]:
		bevestigd=True

GPIO.add_event_detect(pinnen[0],GPIO.FALLING,callback=icb,bouncetime=300)
GPIO.add_event_detect(pinnen[1],GPIO.FALLING,callback=icb,bouncetime=300)

flaskinfos=""
class Dobbel:
	def __init__(self):
		global virtuele
		global gegooid 
	def Schud_de_Dobbelstenen(self):
		#global virtuele
		#global gegooid
		for rand in range(3):
			x=random.randint(1,6)
			virtuele.append(x)
		gegooid=[]
	def Werp_een_steen(self):
		#global virtuele
		#global gegooid
		random_werp=random.randint(1,3)
		print(virtuele[random_werp])
		if len(gegooid)>3:
			foutmelding="Geen stenen meer te werpen \n"
			print(foutmelding)
			flaskinfos+=foutmelding
		else:
			gegooid.append[random_werp]
	def Tel_de_stenen(self):
		#global gegooid
		Eleven=11
		for x in gegooid:
			tellen+=x
		Hoeveel_Tot_Eleven = Eleven - tellen
		if Hoeveel_Tot_Eleven < 11: 
			print("Totaal: ",tellen," Je moet nog ",Hoeveel_Tot_Eleven," Keer gooien om tot het totaal 11 te komen")
			flaskinfos+=" \n Totaal: ",tellen," Je moet nog ",Hoeveel_Tot_Eleven," Keer gooien om tot het totaal 11 te komen"
		else:
			print("Te hoog!!")
			flaskinfos+="Te hoog!! \n"
			print("Wil je opnieuw spelen ? j/n")
			vraag = input()
			if vraag == "j":
				Schud_de_Dobbelstenen()
			else:
				print("Ok")
	def Bekijk_de_stenen(self):
		#global virtuele
		#global gegooid
		for x in virtuele:
			print("Stenen in de hoed ",x)
			flaskinfos+="Stenen in de hoed "+x
		for p in gegooid:
			print("Stenen op tafel = ", p)
			flaskinfos+="Stenen in de hoed "+p
		print("Wil je opnieuw spelen ? j/n")
		vraag = input()
		if vraag =="j":
			Schud_de_Dobbelstenen()
		else:
			GPIO.cleanup()


class Menu:
	spel = Dobbel()
	def get_menuItems(self):
		global scroll
		global bevestigd
		global Menu_Choice
		while True:
			print("- schud de dobbelstenen in de hoed")
			print("- werp een steen")
			print("- tel de stenen op tafel")
			print("- bekijk de stenen on de hoed")
			if bevestigd:
				if scroll == 1:
					Menu_Choice=1
				elif scroll == 2:
					Menu_Choice=2
				elif scroll == 3:
					Menu_Choice=3
				elif scroll == 4:
					Menu_Choice=4
				else:
					print("Gebruik eerst de scroll button") 
				bevestigd=False
			if Menu_Choice==1:
				flaskinfos+="Schude de dobbelstenen in de hoed Menu gekozen \n" 
				spel.Schud_de_Dobbelstenen()
			if Menu_Choice==2:
				flaskinfos+="Werp een steen Menu gekozen \n"
				spel.Werp_een_steen()
			if Menu_Choice==3:
				flaskinfos+="Tel steen op tafel Menu gekozen \n"
				spel.Tel_de_stenen()
			if Menu_Choice==4:
				flaskinfos+="Bekijk de stenen Menu gekozen \n"
				spel.Bekijk_de_stenen()
def ToonInfo():
	global flaskinfos
	return flaskinfos
if __name__=='__main__':
	app.run(host='0.0.0.0')
MenuClass = Menu()
job1=Thread(target=MenuClass.get_menuItems)
job2=Thread(target=ToonInfo)
job1.start()
job2.start()
