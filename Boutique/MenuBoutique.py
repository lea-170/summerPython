# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 22:33:23 2023

@author: Black Baby
"""

import Boutique 

ma_boutique = Boutique.Boutique()

print("Bienvenue dans notre restaurant THE DELIGHTS OF CAMEROON".center(100,"*"))
print("-" * 100)
vouloir_acheter = input("\n---> Souhaitez vous effectuer un achat (oui/non) : ")

#Test de conformité du choix du client
while(vouloir_acheter != "oui" and vouloir_acheter != "non"):
    print("\n--> Veuillez respecter les choix qui vont sont proposés")
    vouloir_acheter = input("\n---> Souhaitez vous effectuer un achat (oui/non) : ")
    
#liste des produits achetés par le client et ses informations complementaires
articles_achetes = []

#Lancement du programme pour les achats du client
ma_boutique.lancement(vouloir_acheter,articles_achetes)

