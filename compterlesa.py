count = 0
text = "Le sénateur, dont il a été parlé plus haut, était un homme entendu qui avait fait son chemin avec une rectitude inattentive à toutes ces rencontres qui font obstacle et qu'on nomme conscience, foi jurée, justice, devoir; il avait marché droit à  son but et sans broncher une seule fois dans la ligne de son avancement et de son intérêt.  C'était un ancien procureur, attendri par le succès, pas méchant homme du tout, rendant  tous les petits services qu'il pouvait à ses fils, à ses gendres, à ses parents, même à des amis; ayant sagement pris de la vie les bons côtés, les bonnes occasions, les bonnes aubaines. Le reste lui semblait assez bête. Il était spirituel, et juste assez lettré pour se croire un disciple d'Epicure en n'étant peut-être qu'un produit de Pigault-Lebrun."
NbdeA = 0

for letter in text:
	if letter== "a" or letter == "à":
		NbdeA += 1

print (NbdeA)