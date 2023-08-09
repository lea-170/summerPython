# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 09:04:39 2023

@author: Black Baby
"""

from pyton0 import *
from math import *

#Menu principal 
print("Bienvenu! Nous implementons ici quelques methodes de calcul mathematiques")

n = int(input("Veuillez saisir \n 1: si vous voulez resoudre une equation du premier degre \n 2: si vous voulez resoudre une equation du second degre \n 3: si vous voulez resoudre un systeme de deux equations à deux inconnues \n 4: si vous voulez determiner le signe d'un produit de deux nombres \n  "))

if(n==1):
    print("Nous allons ici resoudre une equation du premier degre de la forme ax+b=0 ")
    A = float(input("Entrez la valeur de a: "))
    B = float(input("Entrez la valeur de b: "))
    
    #appel de la fonction
    resultat = equation1(A, B)
    print("La solution de cette equation est: " +str(resultat))
elif(n==2):
    print("Nous allons ici resoudre une equation du second degre de la forme ax^2+bx+c=0 ")
    A = float(input("Entrez la valeur de a: "))
    B = float(input("Entrez la valeur de b: "))
    C = float(input("Entrez la valeur de c: "))
    
    #appel de la fonction
    resultat = equation2(A, B, C)
    print("Les solutions de cette equation sont: "+str(resultat))
elif(n==3):
    print("Nous allons ici resoudre un syteme d'equation à deux inconnues")
    print("Notre systeme est de la forme ax+by = c et dx+ey=f")
    
    A = float(input("Entrez la valeur de a: "))
    B = float(input("Entrez la valeur de b: "))
    C = float(input("Entrez la valeur de c: "))
    D = float(input("Entrez la valeur de d: "))
    E = float(input("Entrez la valeur de e: "))
    F = float(input("Entrez la valeur de f: "))
    
    #appel de fonction 
    resulat = systeme(A, B, C, D, E, F)
    print("les solutiosn de ce systeme sont : " +str(resulat))
    
else:
    print("ici nous allons determiner le signe du produit de deux nombres sans calculer le produit")
    A = float(input("Entrez la valeur de a: "))
    B = float(input("Entrez la valeur de b: "))
    
    #appel de la fonction signeProduit
    signeProduit(A, B)
   