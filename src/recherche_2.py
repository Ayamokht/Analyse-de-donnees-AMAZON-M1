# -*- coding: utf-8 -*-
"""

fonction qui permet de retourner des produits triés par prix croissant ou note décroissantes,
 dépendant du choix du consommateur 
         -Input : dataFrame de la fusion des données catégorie et produits)

         -Output : dataFrame trié (en fonction du prix ou des notes) de produits qui pourraient intéresser le consommateur
         (en accord avec la catégorie, la note minimale et le nombre minimal d’unités vendues qu’il a entré)

"""
## Chargement et nettoyage des donnees a partir du module

import pandas as pd
import data_clean as dc

pd.set_option('display.max_columns', None)

fusion= dc.fusion

""" Module recherche_2.py

 fonction qui permet de retourner des produits triés par prix croissant ou note décroissantes,
 dépendant du choix du consommateur 
         -Input : dataFrame de la fusion des données catégorie et produits)

         -Output : dataFrame trié (en fonction du prix ou des notes) de produits qui pourraient intéresser le consommateur
         (en accord avec la catégorie, la note minimale et le nombre minimal d’unités vendues qu’il a entré)

"""
def Tri(df): 

    Tri_par = input("voulez vous trier par prix ou par note (choisissez ‘prix’ ou ‘note’) :").lower() # on demande au Cr s’il veut les produits trié par prix ou par note
    categorie=input("Quelle catégorie voulez-vous ?").lower() #on demande au Cr de choisir une catégorie

    note_min=int(input("Choisissez une note minimale entre 1 et 5 : ")) #On demande au Cr quelle note minimale doivent avoir les produits

    nb_unite_min=int(input("Quel doit être le nombre minimal d'unités vendues ? ")) #Le Cr choisit le nombre minimal de ventes que doit avoir chaque produit

    df = df.loc[(df["category_name"] == categorie) & (df["stars"]>=note_min) & 
                (df["boughtinlastmonth"]>=nb_unite_min)]  #on garde qu’une partie de la DataFrame initiale : que les produits qui respectent les 3 conditions du consommateur (cad les produits qui appartiennent à la catégorie qu’il a choisit, qui ont une note supérieur à la note minimum qu’il a saisi, qui ont un nombre de ventes supérieur au nombre minimal définit par le consommateur 

    if Tri_par=='prix': #si le Cr a choisi de trier par prix le dataFrame contenant les produits qui pourrait l'intéresser 
        df = df.sort_values(by="price",ascending=(True)) #on trie les valeurs du dataFrame par prix croissant (donc du produit le moins cher au plus cher)

    elif(Tri_par=='note'): #si le Cr a choisi de trier par note le dataFrame contenant les produits qui pourraient l’intéresser 
        df = df.sort_values(by="stars",ascending=(False)) #on trie les valeurs du dataFrame par avis décroissant (donc du produit avec le plus d’avis au produit qui en a le moins)      
        
    return df.head(20)

print(Tri(fusion)) 

    #exemple d'utlisation de la fonction : 

 
