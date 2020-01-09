def resCodeBarre():
	with open("barcodes.csv", 'r') as f:
		ligne = f.readline()
		nomProduit = ligne.split(',')[1]
		return nomProduit
