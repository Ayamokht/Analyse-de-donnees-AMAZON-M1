# -*- coding: utf-8 -*-
"""
    PROJET AMAZON: Partie 2

         Data_clean.py : Module du nettoyage de données pour les deux bases de données.
 
"""
import pandas as pd
import data_load as dl

pd.set_option('display.max_columns', None)


A_categories = dl.A_categories
A_products = dl.A_products

##### Nettoyage des deux bases de donnees: ######

def nettoyage(df):
    print(df.isna().sum())

    df = df.fillna("missing")

    if 'id' in df.columns:
        df = df.rename(columns={'id': 'category_id'})

    if 'title' in df.columns:
        df['title'] = df['title'].str.lower()

    if 'category_name' in df.columns:
        df['category_name'] = df['category_name'].str.lower()
        
    for col in df.columns:
        df = df.rename(columns={col: col.lower()})

    df = df.drop_duplicates()

    return df

# Apply the nettoyage function to both DataFrames
A_categories = nettoyage(A_categories)
A_products = nettoyage(A_products)

    
URLVal_Manquante = A_products.loc[A_products['title'] == "missing", 'producturl']
print(URLVal_Manquante)
A_products.loc[URLVal_Manquante.index, 'title'] = '''carlisle foodService products 3646875 flo-thru plastic auto wash brush with flagged nylex bristles, 10" length, green'''
print( A_products.iloc[1206102])


fusion = pd.merge(A_products, A_categories, how="outer", on=["category_id"])
print(fusion.head())
