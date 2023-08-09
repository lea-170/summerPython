# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 10:26:00 2023

@author: Black Baby
"""
import math
#Fonction de resolution d'une equation du premier dégré
def equation1(a,b):
    print("Votre equation est de la forme : " ,a,"x +" ,b)

    if(a==0):
        if(b==0):
            print("cette equation admet une infinite de solution.")
        else:
            print("cette equation n'admet pas de solution.")
    else:
        x = -b/a
        print(x)
        return x
   
    
#Fonction de resoluton d'une equation du second dégré
def equation2(a,b,c):
    print("Votre equation est de la forme : " ,a,"x^2 +" ,b,"x +",c)
    
    if(a==0):
        z = equation1(b, c)
        return z
    else:
        if(b==0):
            if(c==0):
                x=0
                print("cette equation admet pour solution: " ,x)
            elif(c>0):
                print("cette eqaution admet pas de solution reelle.")
            else:
                x= math.sqrt(c) / a
                y= -math.sqrt(c) / a
                print(x,y)
                return x,y
        else:
            if(c==0):
                x=0
                y=equation1(a, b)
                print(x,y)
                return x,y
            else:
                d = b*b-4*a*c
                if(d<0):
                    print("cette equation n'admet pas de solution")
                elif (d == 0):
                    x = -b/(2*a)
                    print("la valeur de x est :" +str(x))
                else:
                    x = (-b + math.sqrt(d))/(2*a)
                    y = (-b- math.sqrt(d))/(2*a)
                    print(x,y)
                    return x,y

            
#Fonction de resolution d'un systeme d'equations à deux inconnues
def systeme(a,b,c,d,e,f):
    #calcul du determinant du systeme
    D = a*e - b*d

    #calcul du determinant sur x
    X = e*c - b*f

    #calcul du determinant sur y
    Y = a*f - c*d

    if(D==0):
        if(X==0 or Y==0):
            print("ce systeme admet une infinité de solution")
        else:
            print("ce systeme n'admet pas de solution")
    else:
        x = X/D
        y = Y/D 
        print(x,y)
        return x,y

#Fonction permettant de determiner le signe du produit de deux nombres 
def signeProduit(a,b):
   if((a==0 or b==0)):
        print("le produit est nulle")
   elif((a>0 and b>0) or (a<0 and b<0)):
        print("le signe de ce produit est positif")
   else:
        print("le signe de ce produit est negatif")
        

    

    
    
    