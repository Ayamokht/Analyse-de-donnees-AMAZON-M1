# -*- coding: utf-8 -*-
"""
Code Principal

"""

import pandas as pd
import os

chemin_actuel = os.getcwd()

# Afficher le répertoire de travail actuel
print("Chemin actuel:", chemin_actuel)
os.chdir("../modules") #allons dans nos modules

import data_clean as dc

fusion= dc.fusion

#Question1:

from recherche_1 import recherche_produit
recherche_produit(fusion)

#exemple:
    #saisir le nom du produit :Battery
    #saisir le nom d une catégorie :Laptop Accessories
    #Choisissez notes, avis ou prix : prix

#Question2: 

from recherche_2 import Tri
Tri(fusion)

# exemple: 
    #voulez vous trier par prix ou par note (choisissez ‘prix’ ou ‘note’) :note
    #Quelle catégorie voulez-vous ?Laptop Accesories
    #Choisissez une note minimale entre 1 et 5 : 4
    #Quel doit être le nombre minimal d'unités vendues ? 10
    
    
#Question3:
    
from recherche_3 import cadeau
cadeau(fusion)

#exemple:
    #Saisir une catégorie : Laptop Accessories
    #Ajouter une nouvelle catégorie
    # => saisir une nouvelle catégorie :  Fabric Decorating
    #Saisir votre budget : 79.99
    #Voulez-vous préciser le type de produit (oui/ non) : oui
    #Si oui, choisissez un type de produit : Battery
    
        