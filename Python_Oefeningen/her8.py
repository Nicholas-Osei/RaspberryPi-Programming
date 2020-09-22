from threading import Thread
import time

counter1=0
counter2=10

def lol():
	global counter1
	while counter1 < 10:
		time.sleep(1)
		counter1+=1
		print("Counter 1: " ,counter1)

def eh():
	global counter2
	while counter2 >=0:
		time.sleep(1)
		counter2-=1
		print("Counter 2: " ,counter2)

job1=Thread(target=lol)
job2=Thread(target=eh)

job1.start()
job2.start()
