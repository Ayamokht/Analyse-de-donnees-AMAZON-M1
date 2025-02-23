#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Question 3 (partie 2) sous forme d'interface graphique

    Description : le programme devra aider un utilisateur à choisir un cadeau
    Input : dataframe de tous les données d’Amazon (fusion qu’on avait fait avec products et categories)
    Output : résultats dans l'interface graphique avec le nom, le lien vers les pages des produits sur Amazon et les images

"""

import os
import pandas as pd
import tkinter as tk
import webbrowser

os.getcwd()

# Importation des données 
A_categories = pd.read_csv("../../Data/amazon_categories.csv", sep=",")
A_products = pd.read_csv("../../Data/amazon_products.csv")

A_categories=A_categories.rename(columns = {'id': 'category_id'})
fusion = pd.merge(A_products,A_categories, how="outer", on=["category_id"])

CAT = [] #création d'une liste vide 

def cadeau():
    global CAT #variable globale
    
    #Création d'un dataframe vide avec les colonnes souhaités
    result = pd.DataFrame(columns=fusion.columns)

    #On fait une boucle à travers la liste CAT pour récupérer les catégories saisies par l'utilisateur 
    for i in CAT:
        categorie = i.get()
        if categorie:
            df1 = fusion.loc[fusion["category_name"] == categorie] #Filtrer fusion pour ne garder que les lignes correspondanst à la catégorie saisie
            result = pd.concat([result, df1]) #concatenation
        else :    
            result = fusion

        
    #On récupère le choix du budget
    budget = choix_budget.get()
    A = result.loc[result["price"] <= float(budget)] # Garder les lignes avec un prix inférieur ou égal au budget
    
    #On récupère le choix du type 
    Proposition_produit = choix_produit.get()
    
    #Si l'utilisateur veut choisir un type de produit
    if Proposition_produit == 'oui':
        Type = choix_Type.get()
        #On filtre les libellés de produit pour garder que le type choisi par l'utilisateur
        #Puis on trie en fonction des notes, des avis, et des meilleurs ventes
        d1 = A[A['title'].str.contains(Type, case=False)]
        d1 = d1.sort_values(['stars', 'reviews', 'isBestSeller'], ascending=[False, False, False])
        
        #On filtre les libellés de produits pour ne garder que les produits dont le titre n'a pas le type spécifié     
        #Puis on trie en fonction des notes, des avis, et des meilleurs ventes
        d2 = A[~A['title'].str.contains(Type)]
        d2 = d2.sort_values(['stars', 'reviews', 'isBestSeller'], ascending=[False, False, False])

        AA = pd.concat([d1, d2]) #concaténation
    
    # Si l'utilisateur ne veut pas spécifier de type, on trie juste les résultats 
    else:
        AA = A.sort_values(['stars', 'reviews', 'isBestSeller'], ascending=[False, False, False])

    #création de la zone de texte
    position1 = 1.0 #position de départ
    position2 = tk.END #position d'arrivée
    zone_texte.delete(position1, position2) #Supprimer la recherche précédente de la 1ère ligne à la dernière ligne

    for index, row in AA.iterrows(): #retourne l’index de la ligne et toutes les données de la ligne sous forme de séries
    #on parcours les lignes du dataframe 
        lien1 = row['productURL'] #on garde pour chaque ligne/série que l'element "productURL" pour avoirs les liens
        lien2 = row['imgUrl']
        zone_texte.insert(position2, row['title']) #on insère à la fin de la zone de texte une seule chaîne de caractère qui est  la concaténation du libellé du produit et du lien
        
        lien_label1 = tk.Label(zone_texte, text=lien1, fg="blue", cursor="hand1")
        #on crée un label qui doit être ajouté à la zone de texte
        lien_label1.bind("<Button-1>", lambda e, l=lien1: lien_cliquable(l))
         #On lie l’évenement “clic gauche” à la fonction “lien_cliquable”. La fonction lambda appelle la fonction “lien_cliquable” lorsque l’événement (clic gauche) est déclenché 

        zone_texte.window_create(position2, window=lien_label1)

        lien_label2 = tk.Label(zone_texte, text=lien2, fg="blue", cursor="hand1")
        #on crée un label qui doit etre ajouté à la zone de texte
        lien_label2.bind("<Button-1>", lambda e, l=lien2: lien_cliquable(l))
          #On lie l’évenement “clic gauche” à la fonction “lien_cliquablet”. La fonction lambda appelle la fonction “lien_cliquable” lorsque l’événement (clic gauche) est déclenché 

        zone_texte.window_create(position2, window=lien_label2)

        zone_texte.insert(tk.END, "\n")

def lien_cliquable(lien): #permet de rendre le lien cliquable : on pourra accéder au site Amazon et à l'image
    webbrowser.open_new(lien) 

def ajouter_categorie(): #fonction appelée lorsque l'utilisateur clique sur le bouton "Saisir une catégorie supplémentaire"
    #on crée un nouveau label et une nouvelle zone de saisie pour que l'utilisateur puisse ajouter une catégorie
    label = tk.Label(fenetre, text="Saisir une nouvelle catégorie :", font=("Arial", 16, "bold"), fg='dark violet')
    label.pack()
    entree = tk.Entry(fenetre)
    entree.pack()
    CAT.append(entree) #cette nouvelle entrée est ajouté à la liste CAT

#création de l'interface 
fenetre = tk.Tk()
fenetre.title("cadeau")
fenetre.geometry('900x1200')

fenetre.configure(bg='pink')

Titre_label = tk.Label(fenetre, text="Trouver le Cadeau Idéal !", font=("Palatino", 30, "bold"), fg='MediumPurple1')
Titre_label.pack()

#Création du label catégorie (correspond au 1er choix de catégorie)
cat_label = tk.Label(fenetre, text="Saisir une catégorie :", font=("Arial", 16, "bold"), fg='dark violet')  # Violet foncé
cat_label.pack()
choix_cat = tk.Entry(fenetre) #création d'une zone de saisie permettant la saisie de l'utilisateur
choix_cat.pack()
CAT.append(choix_cat) #cette nouvelle entrée est ajouté à la liste CAT

#Bouton qui permet l'ajout d'une ou plusieurs catégorie selon le choix de l'utilisateur
bouton_ajout_cat= tk.Button(fenetre, text="Ajouter une catégorie supplémentaire",  font=("Arial", 10, "bold"), fg='dark violet',command=ajouter_categorie)
bouton_ajout_cat.pack()

#Création du label budget dans lequel l'utilisateur pourra saisir son budget 
budget = tk.Label(fenetre, text="Saisir votre budget :", font=("Arial", 16, "bold"), fg='dark violet')
budget.pack()
choix_budget = tk.Entry(fenetre)
choix_budget.pack()

#Création du label type qui permet à l'utilisateur de préciser si il veut un type de produit ou non
Proposition_produit = tk.Label(fenetre, text="voulez-vous préciser le type de produit (oui/non) :",  font=("Arial", 16, "bold"), fg='dark violet')
Proposition_produit.pack()
choix_produit = tk.Entry(fenetre)
choix_produit.pack()

#Création d'un nouveau label en réponse au label précédent: si l'utilisateur veut un type de produit, il le précisera dans ce label
type_produit = tk.Label(fenetre, text="Si oui choisissez un type de produit :", font=("Arial", 16, "bold"), fg='dark violet')
type_produit.pack()
choix_Type = tk.Entry(fenetre)
choix_Type.pack()

#Création d'un bouton recherche qui appelle la fonction cadeau : 
#lorsque l'utilisateur aura saisit ses critères, il appuiera sur ce bouton afin de lancer la recherche
Bouton_cadeau = tk.Button(fenetre, text="C'est parti !", font=("Arial", 18, "bold"), fg='dark violet', command=cadeau)
Bouton_cadeau.pack()

#Création d'une zone de texte qui affichera les résultats de la recherche (liée à la fonction cadeau)
zone_texte = tk.Text(fenetre, width=90, height=30)
zone_texte.pack()

fenetre.mainloop()

zone_texte.configure(font=("Times New Roman", 25, "italic")) #configuration d'une police de texte

fenetre.mainloop()









