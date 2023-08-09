# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 20:49:02 2023

@author: Black Baby
"""

#definition de la classe facture 
class facture:
    #constructeur de la classe
    def __init__(self,date,heure):
        self.date = date
        self.heure = heure
        # creation et fermeture automatique du fichier
        fichier = open("facture du {} {}.txt".format(date, heure),"w")
        fichier.close()
    #fonction permettant d'initialiser la facture
    def initialisation(self): 
        fichier = open("facture du {} {}.txt".format(self.date, self.heure),"w")
        # ecriture dans le fichier
        fichier.write("THE DELIGHTS OF CAMEROON".center(50,"*"))
        fichier.write("\n\nDate: {}".format(self.date))
        fichier.write("\n\nHeure: {}".format(self.heure))
        fichier.write("\n{:<30}{:<30}{:<30} {:<30}".format("Nom", "Quantite","Prix unitaire","Total"))
        fichier.close()
        
    def remplissage_des_articles(self,articles_achetes,total_achat):
        fichier = open("facture du {} {}.txt".format(self.date, self.heure),"a")
        for i in range(len(articles_achetes)):
            Article,Quantite,Prix_unitaire,Total = articles_achetes[i]
            fichier.write("\n{:<30}{:<30}{:<30} {:<30}".format(Article,Quantite,Prix_unitaire,Total))
        fichier.write("\n -------------------------------------------------------------------------------------------------")
        fichier.write("\n{:<120} {}".format("Total",total_achat))
        
        fichier.close()
        
        

        
