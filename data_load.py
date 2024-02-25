# -*- coding: utf-8 -*-
"""
 PROJET AMAZON: Partie 2
 Chargement des bases de données.
 
 """

import pandas as pd

A_categories_Base = pd.read_csv("../Data/amazon_categories.csv")
A_products_Base = pd.read_csv( "../Data/amazon_products.csv")
   
    
    # deep copy des dataframes pour ne pas toucher à la base de données de base
A_categories = A_categories_Base.copy(deep=True)
A_products = A_products_Base.copy(deep=True)
    