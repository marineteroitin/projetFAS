#attention mettre le driver grovepi.py dans le meme dossier sinon marche pas
import time
import grovepi

# Connect the Grove Button to digital port D4
# SIG,NC,VCC,GND
button = 4
print ("je suis dans le programme bouton \n")
grovepi.pinMode(button,"INPUT")

for x in range(10):
    try:
        print(grovepi.digitalRead(button))
        time.sleep(1)

    except IOError:
        print ("Error\n")
