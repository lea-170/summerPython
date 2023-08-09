# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 10:06:24 2023

@author: Black Baby
"""

t = ["Nom", "Maths","Physique","Chimie","Anglais","Français","Moyenne","Rang"]
t1 = ["Lea",15,17,18,19,17]
t2 = ["Hervé",10,11,16,9,12]
t3 = ["Celeste",12,15,12,10,11]
t4 = ["Judith",17,10,11,13,8]
t5 = ["Franck",12,10,11,8,10]
t6 = ["Manou",13,12,16,15,10]
t7 = ["Joyce",12,19,10,10,7]
t8 = ["Edmond",12,18,15,14,11]
t9 = ["Hugolin",18,15,10,9,10]
t10 = ["Blaise",12,18,15,14,11]

L = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]

#boucle permettant de calculer la moyenne
for i in range(len(L)):
    somme = 0
    for j in range(1,len(L[i])):
    	somme += L[i][j]

    moyenne = somme / (len(L[i]) - 1)
    L[i].append(moyenne)



L.sort(key = lambda t: t[-1])# on trie ici le tableau de façon croissante suivante la plus grande moyenne(L[i][-1])
L.reverse() # on renverse le tableau de sorte a ce que ça soit rangé par ordre décroissant

rang = 1

moyPrecedente = L[0][-1]
L[0].append(rang)
rang += 1

#Ajout du rang dans la liste
for i in range(1, len(L)):
	if(moyPrecedente == L[i][-1]):
		L[i].append(L[i-1][-1])
		rang +=1
	else:
		L[i].append(rang)
		rang +=1

	moyPrecedente = L[i][-2]
fichjier = open("Barbillard.txt","w")
for i in range(len(t)):
    print("{:<20}".format(t[i]),end = "")
print()
print("-"*200)

# affichage de notre liste des listes lignes par lignes 
for i in range(len(L)):
	for j in range(len(L[i])):
		print("{:<20}".format(L[i][j]),end = "|")
    
  
	print("-"*200)

        