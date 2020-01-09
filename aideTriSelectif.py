#-*- coding: utf-8 -*-
# comande necessaire pour modifier notre google sheet 
import gspread
import json
# necessaire pour lire le QrCode
import barcode_scanner_video
import rechercheFichier
# necessaire pour le reste
import progEcran
import grovepi
import time
import picamera
import datetime
from oauth2client.service_account import ServiceAccountCredentials

json_key = json.load(open('Projet FAS-f4a99ef2e506.json'))
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('projet-fas-3d5e22103d13.json', scope)

gc = gspread.authorize(credentials)

sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1-BfCCYAM3PoP42sAtFzQJHxhFZP3DcGJynj8Qv13fH8/edit?usp=sharing')
ws = sht2.worksheet('BDFAS')
#---------------------------------------------------------#

button = 4
grovepi.pinMode(button,"INPUT")

while True:
	try:
		if grovepi.digitalRead(button): #si j'appuie sur le bouton
			progEcran.setText("Bonjour placer  le code barre")
			time.sleep(3)
			progEcran.setText("a 10cm de la \n camera")
			time.sleep(3)
			progEcran.setText("Scannez le \n QrCode dans:")
			time.sleep(1)
			progEcran.setText("3")
			time.sleep(1)
			progEcran.setText("2")
			time.sleep(1)
			progEcran.setText("1")
			time.sleep(1)
			progEcran.textCommand(0x01) #effacer l'ecran

			barcode_scanner_video.rechCodeBarre()

			progEcran.setText("analyse en cours")
			time.sleep(3)
			qrCode = rechercheFichier.resCodeBarre()
			
			#programme concernant BD
			
			codeBarre_list = ws.col_values(1)

			if(qrCode in codeBarre_list) :
		
				#chercher les coordonees de la cellule ou se trouve mon codeBarre
	
				cell = ws.find(qrCode)

				#recuperer le nom du produit correspondant au code barre
				nomProd = ws.cell(cell.row,cell.col+1).value 

				#recuperer la couleur de la poubelle du produit correspondant au code barre
				couleurPoubelle = ws.cell(cell.row,cell.col+2).value 

				#modifier les stats
				if couleurPoubelle == "Jaune":
					ws.update_acell('F2',int(ws.acell('F2').value)+1)
				elif couleurPoubelle == "Bleu":
       					ws.update_acell('F3',int(ws.acell('F3').value)+1)
				elif couleurPoubelle == "Vert":
       					ws.update_acell('F4',int(ws.acell('F4').value)+1)
				else: #dernier cas marron
	       				ws.update_acell('F5',int(ws.acell('F5').value)+1)
 
				#afficher nom et couleur a l’utilisateur
				#ajuster le texte en dessous pour qu'il rentre dans l'ecran
				progEcran.setText("jeter le" + nomProd + "dans la poubelle" + couleurPoubelle)
				time.sleep(3)

			else :
				progEcran.setText("Qrcode inconnu")
				time.sleep(3)
				progEcran.setText("instructions: ")
				time.sleep(3)
				progEcran.setText("verre ->\npoubelle verte")
				time.sleep(3)
				progEcran.setText("plastique ->\npoubelle jaune")
				time.sleep(3)
				progEcran.setText("papier,carton ->\npoubelle bleu")
				time.sleep(3)
				progEcran.setText("autre ->\npoubelle marron")
				time.sleep(3)
				progEcran.setText("Un petit geste\nau quotidien")
				time.sleep(3)
				progEcran.setText("un grand geste\npour la planete")
				time.sleep(3)
				progEcran.textCommand(0x01) #effacer l'ecran
			
	except IOError:
                print("erreur")
