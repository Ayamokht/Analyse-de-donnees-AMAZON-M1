# -*- coding: utf-8 -*-
"""
Question 3: Partie2
 Le programme aide l'utilisateur à choisir un cadeau en lui posant des questions sur ses préférences,
 comme la catégorie de produits, le budget, et le type de cadeau recherché. 
 Ensuite, il suggère des idées de cadeaux en favorisant les produits populaires, 
 bien notés et avec beaucoup d'avis positifs. L'utilisateur a la possibilité de ne pas répondre à toutes les questions.

"""
import pandas as pd
import data_clean as dc

fusion= dc.fusion

"""
 fonction:  aide un utilisateur à choisir un cadeau. 
 
     - input : dataframe de tous les données d’Amazon (fusion qu’on avait fait avec products et categories)
     
     - Output : cela renvoit un dataFrame avec les produits qui pourraient intéresser le consommateur en fonction de ses critères 
"""

def cadeau(df): 
    result = {'asin': [],
        'title': [],
        'imgUrl': [],
        'productURL': [],
        'stars': [],
        'reviews': [],
        'price': [],
        'listPrice': [],
        'category_id': [],
        'isBestSeller': [],
        'boughtInLastMonth': [],
        'category_name': []}
    result = pd.DataFrame(result) #on crée un dataFrame vide

#on met choisit le type de chaque variable 
    result['asin'] = result['asin'].astype(str)
    result['title'] = result['title'].astype(str)
    result['imgUrl'] = result['imgUrl'].astype(str)
    result['productURL'] = result['productURL'].astype(str)
    result['stars'] = result['stars'].astype(float)
    result['reviews'] = result['reviews'].astype(int)
    result['price'] = result['price'].astype(float)
    result['listPrice'] = result['listPrice'].astype(float)
    result['category_id'] = result['category_id'].astype(int)
    result['isBestSeller'] = result['isBestSeller'].astype(bool)
    result['boughtInLastMonth'] = result['boughtInLastMonth'].astype(int)
    result['category_name'] = result['category_name'].astype(str)
    
    CAT = []  #On crée une liste vide
#pas oublier tt mettre en minuscule
    # Boucle pour demander à l'utilisateur d'entrer une catégorie à la fois
    while True: #boucle qui continue tant qu’on l'arrête pas avec break 
        categorie = input("Entrez une catégorie (ou 'non' pour terminer) : ").lower() #on ajoute une catégorie tant qu’on veut
        if categorie == 'non':#ajouter len()
            break  #si le consommateur ne veut pas entrer de catégorie on arrête la boucle
        CAT.append(categorie) #on ajoute les catégories que le Cr veut dans la liste vide qu’on a crée  
        if len(CAT) != 0: #s’il y’a des catégories dans la liste (donc si le Cr a fait un choix)
            for i in CAT: #pour chaque élément de la liste donc pour chaque catégorie 
            	df = df.loc[df["category_name"] == i] # à chaque fois on garde que les produits qui correspondent à catégorie choisi par le Cr
            	result = pd.concat([result, df]) #on ajoute dans les result tous les produits répondant à notre catégorie
        else: 
            result=df  

    budget=float(input("quel est votre budget ?"))#ajouter la possibilité de ne pas en mettre 

    A=result.loc[result["price"]<= budget] #Parmi les produits qui respectent les catégories choisi par le Cr on garde que ceux qui respectent le budget
    choix_T = input("voulez vous préciser le type du produit( oui / non) : ").lower()
  
    if choix_T == 'oui':
        Type=input("choisissez un type : ").lower()
        d1 = A[A['title'].str.contains(Type, case=False)] #on garde que les produits dont le titre contient le type choisi par le Cr
        d1 = d1.sort_values(['stars','reviews','isBestSeller'], ascending=[False,False,False])       
         #on trie tous les produits dont le titre contient le type choisi par le Cr, d’abord par note, ensuite par avis et enfin par BestSeller (false ou true et décroissant met les true avant)

        d2 = A[~A['title'].str.contains(Type)] #on récupère tous les produits dont le titre ne contient pas le type choisi par le Cr
        d2 = d2. sort_values(['stars','reviews','isBestSeller'], ascending=[False,False,False])       
         #on trie tous les produits dont le titre ne contient pas le type choisi par le Cr, d’abord par note (décroissant), ensuite par avis (décroissant)  et enfin par BestSeller (false ou true et décroissant met les true avant)
        
        AA = pd.concat([d1, d2]) #on rassemble les deux dataframe en mettant  au dessus celui contenant les produits dont le titre contient le type choisi
  
    else :
        AA=A.sort_values(['stars','reviews','isBestSeller'], ascending=[False,False,False]) #si le Cr ne veut pas entrer de type on trie les produits qui respectaient notre budget initial et nos catégories choisit, d’abord par note (décroissant), ensuite par avis (décroissant) et enfin par BestSeller (false ou true et décroissant met les true avant)  

    return AA.head(20)
 
resultat_cadeau=cadeau(fusion)
print(resultat_cadeau)

