#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Question 2 (partie 2) sous forme d'interface graphique

    Description : L’utilisateur saisit un catégorie, une note minimale et un nombre minimal d’unités vendues: 
        le programme doit retourner les produits correspondants, par prix ou par note.
    Input : dataframe de tous les données d’Amazon (fusion qu’on avait fait avec products et categories)
    Output : résultats dans l'interface graphique avec le nom, le lien vers les pages des produits sur Amazon et les images

"""

import os
import pandas as pd
import seaborn as sns
import webbrowser
import tkinter as tk
 
# avoir le répertoire de travail
os.getcwd()

# Importation des données 
A_categories = pd.read_csv("../../Data/amazon_categories.csv", sep=",")
A_products = pd.read_csv("../../Data/amazon_products.csv")

A_categories=A_categories.rename(columns = {'id': 'category_id'})
fusion = pd.merge(A_products,A_categories, how="outer", on=["category_id"])

def Tri(df=fusion):
    Tri_par = choix_tri.get()#la fonction get permet de récupérer la valeur entrée dans l'interface par l'utilisateur
    categorie = choix_cat.get()
    note_min = int(choix_note.get())
    nb_unite_min = float(choix_nb.get())
    df = df.loc[(df["category_name"] == categorie) & (df["stars"]>=note_min) & 
                (df["boughtInLastMonth"]>=nb_unite_min)] 

    if Tri_par=='prix': 
        df = df.sort_values(by="price",ascending=(True)) 

    elif(Tri_par=='note'): 
        df = df.sort_values(by="stars",ascending=(False))      
    
    position1 = 1.0 #on définit la position 1 dans la zone de texte (c’est le début)
    position2 = tk.END #on définit la position 2 dans la zone de texte (c’est la fin)
    zone_texte.delete(position1, position2) #on supprime le contenu actuel de la zone de texte (de la position1 à la position2) lorsque l’utilisateur veut changer ses critères afin d’afficher de nouveaux résultats 

    for index, row in df.iterrows(): #on parcours les lignes du DataFrame
#df.iterrows() retourne l’index de la ligne et toutes les données de la ligne sous forme de série
        lien1 = row['productURL'] #on récupère le lien de chaque produit 
        lien2 = row['imgUrl'] #on récupère les liens des images de chaque produit
        titre = row['title'] #on récupère le nom de chaque produit
        zone_texte.insert(position2, titre) #on affiche le nom de chaque produit dans la zone de texte
        
        label1 = tk.Label(zone_texte, text=lien1, fg="blue", cursor="hand1") #on crée un label avec l’URL du produit
        label1.bind("<Button-1>", lambda e, l=lien1: ouvrir_lien(l)) #On lie l’évenement “clic gauche” à la fonction “lien_ouvert”. La fonction lambda appelle la fonction “lien_ouvert” lorsque l’événement (clic gauche) est déclenché 
        zone_texte.window_create(position2, window=label1) #on ajoute le label1 contenant l’URL du produit dans la zone de texte à la position 2 (c’est-à-dire à la fin du texte actuel)
#on affiche donc des liens cliquables pour chaque produit

        label2 = tk.Label(zone_texte, text=lien2, fg="blue", cursor="hand1") #on crée un label avec l’URL image du produit
        label2.bind("<Button-1>", lambda e, l=lien2: ouvrir_lien(l)) #On lie l’évenement “clic gauche” à la fonction “lien_ouvert”. La fonction lambda appelle la fonction “lien_ouvert” lorsque l’événement (clic gauche)  est déclenché 
        zone_texte.window_create(position2, window=label2) #on affiche donc des liens cliquables pour chaque produit

        zone_texte.insert(position2, "\n") #à chaque fois qu’on insère les informations pour un produit , on saute une ligne

def ouvrir_lien(l):
    webbrowser.open_new(l) #on ouvre chaque lien dans le navigateur (lorsqu’un clique gauche a lieu)

fenetre = tk.Tk () #création de la fenetre principale
fenetre.title("tri") #on donne un titre à cette fenetre
fenetre.geometry('900x1200') #on choisit la dimension

Titre_label = tk.Label(fenetre, text="Trouver le Cadeau Idéal !", font=("Palatino", 30, "bold"), fg='MediumPurple1') #on crée un label pour le titre tout en haut de la page

Tri_par = tk.Label(fenetre, text="tri par prix ou note ?",font=("Palatino", 30, "bold"), fg='MediumPurple1') #on crée un label pour demander à l’utilisateur comment il souhaite trier
Tri_par.pack() #on ajoute le label dans la fenetre principale
choix_tri = tk.Entry(fenetre) #l’utilisateur doit entrer son choix de tri ici
choix_tri.pack()

categorie = tk.Label(fenetre, text="Saisir une catégorie ?",font=("Palatino", 30, "bold"), fg='MediumPurple1')
categorie.pack()
choix_cat = tk.Entry(fenetre)
choix_cat.pack()

note_min = tk.Label(fenetre, text="Saisir une note entre 1 à 5",font=("Palatino", 30, "bold"), fg='MediumPurple1')
note_min.pack()
choix_note = tk.Spinbox(fenetre, from_=1, to=5)
choix_note.pack()

nb_unite = tk.Label(fenetre, text="Saisir un nombre minimum d'unités vendues",font=("Palatino", 30, "bold"), fg='MediumPurple1')
nb_unite.pack()
choix_nb = tk.Entry(fenetre)
choix_nb.pack()

Bouton_trier = tk.Button(fenetre, text="Trier", font=("Palatino", 30, "bold"), fg='MediumPurple1', command=Tri) #on crée un bouton qui appelle la fonction “Tri” lorsqu’il est cliqué
Bouton_trier.pack()

zone_texte = tk.Text(fenetre, width=150, height=40) #création de la zone de texte qui contient les résultats
zone_texte.pack()

fenetre.mainloop()
