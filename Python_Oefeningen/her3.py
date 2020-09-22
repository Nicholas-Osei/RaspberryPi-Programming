import urllib.request

webpagina = urllib.request.urlopen('https://www.meteo.be/nl/antwerpen')
ip_html = webpagina.read()
webpagina.close()

Con=str(ip_html)

locate="temp"

lol = Con.find(locate)+len(locate)+2

pos = Con[lol:lol+20]

print(pos)

if pos[1].isdigit():
	print("Hurray")
else :
	print("Not a digit")
