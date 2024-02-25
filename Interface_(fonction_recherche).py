#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Question 1 (partie 2) sous forme d'interface graphique

    Description : L’utilisateur saisit un nom de produit et une catégorie : 
        le programme doit retourner les produits par notes/ nombre d’avis 
        décroissants ou par prix, selon ce que l’utilisateur aura choisi. 
        S’il y a beaucoup de résultats, n’afficher que les 20 premiers.
    Input : dataframe de tous les données d’Amazon (fusion qu’on avait fait avec products et categories)
    Output : résultats dans l'interface graphique avec le nom, le lien vers les pages des produits sur Amazon et les images

"""

import os
import pandas as pd
import webbrowser
import tkinter as tk
 
# avoir le répertoire de travail
os.getcwd()

# Importation des données 
A_categories = pd.read_csv("../../Data/amazon_categories.csv", sep=",")
A_products = pd.read_csv("../../Data/amazon_products.csv")

A_categories=A_categories.rename(columns = {'id': 'category_id'})
fusion = pd.merge(A_products,A_categories, how="outer", on=["category_id"])

def recherche_produit():
    nom_produit = choix_produit.get() #la fonction get permet de récupérer la valeur entrée dans l'interface par l'utilisateur
    nom_categorie = choix_categorie.get()
    choix = choix_critere.get()

    # Filtrer le dataframe en fonction des valeurs saisies
    df1 = fusion.loc[fusion["category_name"] == nom_categorie] 
    df1 = df1[df1['title'].str.contains(nom_produit, case=False)]
    
    # En fonction du critère de tri choisi par l'utilisateur, trier le dataframe
    if choix == 'notes':
        df1 = df1.sort_values(by="stars", ascending=True)
    elif choix == 'avis':
        df1 = df1.sort_values(by="reviews", ascending=False)
    elif choix == 'prix':
        df1 = df1.sort_values(by="price", ascending=True)
    else:
        print("Le choix saisi est invalide. Les produits ne sont pas triés.")

    position1= 1.0 #on définit la position 1 dans la zone de texte (c’est le début)
    position2= tk.END #on définit la position 2 dans la zone de texte (c’est la fin)
    zone_texte.delete(position1, position2) #on supprime le contenu actuel de la zone de texte (de la position1 à la position2) lorsque l’utilisateur veut changer ses critères afin d’afficher de nouveaux résultats 
    
    for index, row in df1.iterrows():  #on parcours les lignes du DataFrame
#df.iterrows() retourne l’index de la ligne et toutes les données de la ligne sous forme de série
        lien1 = row['productURL'] #on garde pour chaque ligne que l'element "productURL" pour avoirs les liens
        lien2 = row['imgUrl'] #on garde pour chaque ligne que l'élement "imgUrl" pour avoir les liens des images
        titre = row['title'] #on récupère le nom de chaque produit
        zone_texte.insert(position2, row['title']) #on affiche le nom de chaque produit dans la zone de texte
        
        lien_label1 = tk.Label(zone_texte, text=lien1, fg="blue", cursor="hand1") #on crée un label avec l’URL du produit
        lien_label1.bind("<Button-1>", lambda e, l=lien1: lien_cliquable(l)) #On lie l’évenement “clic gauche” à la fonction “lien_ouvert”.
        #La fonction lambda appelle la fonction “lien_ouvert” lorsque l’événement (clic gauche) est déclenché 
        zone_texte.window_create(position2, window=lien_label1) #on ajoute le label1 contenant l’URL du produit dans la zone de texte 
        #à la position 2 (c’est-à-dire à la fin du texte actuel) #on affiche donc des liens cliquables pour chaque produit
        
        lien_label2 = tk.Label(zone_texte, text=lien2, fg="blue", cursor="hand1")  #on crée un label avec l’URL image du produit
        lien_label2.bind("<Button-1>", lambda e, l=lien2: lien_cliquable(l)) #On lie l’évenement “clic gauche” à la fonction “lien_ouvert”. 
        #La fonction lambda appelle la fonction “lien_ouvert” lorsque l’événement (clic gauche)  est déclenché 
        zone_texte.window_create(position2, window=lien_label2) #on affiche donc des liens cliquables pour chaque produit

        zone_texte.insert(tk.END, "\n") #à chaque fois qu’on insère les informations pour un produit , on saute une ligne

def lien_cliquable(l):
    webbrowser.open_new(l) #on ouvre chaque lien dans le navigateur (lorsqu’un clique gauche a lieu)
    
# Création la fenêtre principale
fenetre = tk.Tk() #création de la fenetre principale
fenetre.title("Choisir un produit, une catégorie et un critère") #on donne un titre à cette fenetre
fenetre.geometry('900x1200') #on choisit la dimension

Titre_label = tk.Label(fenetre, text="TRIER LES PRODUIT !", font=("Palatino", 20, "bold"), fg='MediumPurple1')  #on crée un label pour le titre tout en haut de la page

label_produit = tk.Label(fenetre, text='Saisir un produit',font=("Palatino", 20, "bold"), fg='MediumPurple1') #on crée un label pour demander à l’utilisateur un produit
label_produit.pack()  #on ajoute le label dans la fenetre principale
choix_produit = tk.Entry(fenetre)  #l’utilisateur doit entrer son choix de produit ici
choix_produit.pack()

label_categorie = tk.Label(fenetre, text='Saisir une catégorie', font=("Palatino", 20, "bold"), fg='MediumPurple1')
label_categorie.pack()
choix_categorie = tk.Entry(fenetre)
choix_categorie.pack()

label_critere = tk.Label(fenetre, text='Saisir notes, avis ou prix :', font=("Palatino", 20, "bold"), fg='MediumPurple1')
label_critere.pack()
choix_critere = tk.Entry(fenetre)
choix_critere.pack()

#création d'un bouton de recherche 
bouton_rechercher = tk.Button(fenetre, text="Rechercher",font=("Palatino", 20, "bold"), fg='MediumPurple1', command=recherche_produit) #on crée un bouton qui appelle la fonction "recherche_produit” lorsqu’il est cliqué
bouton_rechercher.pack()

# Création d'une zone de texte pour afficher les résultats 
zone_texte = tk.Text(fenetre, height=150, width=140) #création de la zone de texte qui contient les résultats
zone_texte.pack()

fenetre.mainloop()
