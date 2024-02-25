# -*- coding: utf-8 -*-
"""
Projet AMAZON: Partie2
    Question1: 
       
        L’utilisateur saisit un nom de produit et une catégorie : le programme doit retourner les produits par notes/
        nombre d’avis décroissants ou par prix, selon ce que l’utilisateur aura choisi. S’il y a beaucoup de résultats,
        n’afficher que les 20 premiers.
        
"""
## Chargement et nettoyage des donnees a partir du module

import pandas as pd
import data_clean as dc

fusion= dc.fusion
"""
  Module recherche_1.py      
"""
def recherche_produit(df1): #prend en défaut la table fusion

    nom_produit_0=input("saisir le nom du produit :").lower()
    nom_categorie_0=input('saisir le nom d une catégorie :').lower()
    choix_0 = input("Choisissez notes, avis ou prix : ").lower()  
    
      
    df1 = df1.loc[df1["category_name"] == nom_categorie_0] 
        #filtrer le dataframe df1 en fonction de la colonne "nom_categorie" choisie par l’utilisateur
    df1 = df1[df1['title'].str.contains(nom_produit_0, case=False)]  
        #conserver les lignes de la colonne ‘title’ contenant que le nom du produit saisie par l’utilisateur(nom_produit)
        #en fonction du critère de tri choisi par l’utilisateur, on trie en fonction de la colonne associée 
    if choix_0=='notes':
       df1 = df1.sort_values(by="stars",ascending=(True))
    elif choix_0=='avis':
       df1  = df1.sort_values(by="reviews",ascending=(False))
    elif choix_0 =='prix':
        df1 = df1.sort_values(by="price",ascending=(True))

    else:
        print("Le choix saisi est invalide, les produits ne sont pas triés. Voici les " + str(nom_produit_0) +
              " appartenant à la catégorie " + str(nom_categorie_0))
        #si l’utilisateur ne rentre pas de critère de tri ou rentre une mauvaise syntaxe
        #alors un message sera affiché et retournera les libellés des produits triés seulement 
        #par le nom de produit et le nom de catégorie
    df1=df1 ['title'].reset_index(drop=True)

    return df1.head(20)

print(recherche_produit(fusion))

#exemple d'utilisation de la focntion
recherche_produit(fusion)