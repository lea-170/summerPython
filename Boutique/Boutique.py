# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:37:35 2023

@author: Black Baby
"""
import facture
import datetime
import csv

class Boutique:
    
    #Constructeur 
    def __init__(self):
        self.articles_en_stocks = []
    
    #Fonction permattant de charger nos articles dans une liste 
    def articles(self):
        #ouverture et acces en lecture du fichier Articles
        fichier = open("Articles.csv","r")
        articles_en_stocks = []
        #lecture de nos articles
        articles_en_stocks = list(csv.reader(fichier,delimiter = ";"))
        fichier.close()
        self.articles_en_stocks = articles_en_stocks

    #Fonction permettant d'afficher les elements en les separant d'au plus dix caracteres
    def affichage_articles(self):
        print("{:<30}{:<30}{:<30}{:<30}".format("N°","Articles","Prix Uniatire","Quantité"))  
        print()
        for i in range(1,len(self.articles_en_stocks)-1):
            print("{:<30}".format(i),end="")
            for j in range(len(self.articles_en_stocks[i])-1):
                print("{:<30}".format(self.articles_en_stocks[i][j]),end="" )
            print("\n")
           
    #Fonction permettant le choix de l'article
    def choixArticles(self,articles_achetes):
        reponse = True
        while(reponse):
            n = input("---> Voulez-vous un de nos articles? (repondez par oui/non) \t")
            if(n == "oui"):       
                choixProduit = int(input("---> Veuillez saisir le numero du produit que vous desirez: \t"))
                
                if((choixProduit < 0) or (choixProduit >=(len(self.articles_en_stocks)-1))): #cas numero invalide
                    print("Votre choix est indisponible.\n Veuillez entrer un numero dans la liste")
                    
                else: # cas numero valide
                  #condition permettant de savoir si le choix de l'utilisateur est disponible en stock
                  if(self.articles_en_stocks[choixProduit][1] == "0"):
                      print("Désolé! Le choix que vous avez fait n'est pas disponible ne stock.")
                  else:
                      QuantiteProduit = int(input("---> Quelle quantité de ce produit voulez-vous? \t"))
                      
                      #condition permettant de verifier si la quantité en stock est suffisante pour le client
                      if(QuantiteProduit > int(self.articles_en_stocks[choixProduit][1])):
                          print()
                          print("Désolé nous n'avons pas suffisamment de produit selon votre demande.")
                      else:
                          Prix = QuantiteProduit*int(self.articles_en_stocks[choixProduit][1])
                          print("Votre Net-à-payer est: " +str(Prix))
                          
                          #retranchement de la quantite prise dans le fichier csv
                          self.articles_en_stocks[choixProduit][2]
                          articles_achetes.append(
                              [
                                  self.articles_en_stocks[choixProduit][0],str(QuantiteProduit),self.articles_en_stocks[choixProduit][1],str(Prix)
                               ]
                              )
                          #Modification de notre liste de stocks
                          self.articles_en_stocks[choixProduit][2] = str(int(self.articles_en_stocks[choixProduit][2]) - QuantiteProduit)
                         
                  reponse = True   
                    
            else:
                reponse = False 
                break

    #fonction permettant de calculer le prix totals des achats effectués
    def total_achats(self,articles_achetes):
        total_achat = 0
        for i in range(len(articles_achetes)):
            total_achat = total_achat + int(articles_achetes[i][3])
        return total_achat
    
     #focntion de mise a jour de la quantite des produits apres un achat dans le fichier csv       
    def Mise_a_jour(self):
        fichier = open("Articles.csv" ,"w",newline = "")
        writer = csv.writer(fichier, delimiter = ";")
        
        for i in range(len(self.articles_en_stocks)):
            writer.writerow(self.articles_en_stocks[i])
            
    #Lancement de la boutique 
    def lancement(self, vouloir_acheter, articles_achetes):
        
        if(vouloir_acheter == "oui"):
            # chargement des articles 
             self.articles()
             
             #affichage des articles 
             print(" Voici nos articles ".center(100,"*"))
             print()
             self.affichage_articles()
             
             # achat de l'article 
             self.choixArticles(articles_achetes)
                
             #Calcul du total
             prix_a_payer = self.total_achats(articles_achetes)

             #Etablissement de la facture
             if prix_a_payer != 0:
                #Creation de l'objet facture du client
                date_et_heure = (str(datetime.datetime.now())).split(" ") #On recupere la date(position 0 dans la liste) et l'heure(poisiton 1) actuelles
                date_et_heure[1] = date_et_heure[1].replace(":","-") #On retire : car ce caractere n'est pas autorise dans un nom de fichier windows
                facture_client = facture.facture(date_et_heure[0], date_et_heure[1])
                facture_client.initialisation()

                #Remplissage de la facture
                facture_client.remplissage_des_articles(articles_achetes,prix_a_payer)
                
             #Mise a jour du stock apres tous les achats
             self.Mise_a_jour()
         
                
        else:
            print("\n---> Merci. Au plaisir de vous revoir...")
    

         
     
 


    


