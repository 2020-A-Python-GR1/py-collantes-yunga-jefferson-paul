# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:38 2020

@author: jeffe
"""



import numpy as np
import pandas as pd 

lista_numeros = [1,2,3,4]
tupla_numeros = [1,2,3,4]
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(
    lista_numeros)

series_b = pd.Series(
    tupla_numeros)

series_c = pd.Series(
    np_numeros)

series_d = pd.Series(
    [True,
    False,
    12,
    12.12,
    "Jefferson",
    None,
    (1),
    [2],
    {"Nombre": "Jefferson"}
    ])

print (series_d[3])

lista_ciudades = [
    "Amabato",
    "Cuenca",
    "Loja",
    "Quito"]

series_ciudad = pd.Series(
    lista_ciudades,
    index=[
        "A",
        "C",
        "L",
        "Q"])
#se puede acceder con indices o con la posiciona
print(series_ciudad[3])
print(series_ciudad["C"])

valores_ciudad = {
    "Ibarra":9500,
    "Guayaquil": 100000,
    "Cuenca":70000,
    "Quito": 80000,
    "Loja":3000
    }

series_valor_ciudad = pd.Series(
    valores_ciudad)


ciudad_menor_5k = series_valor_ciudad < 5000
print (type(valores_ciudad))
print (type(ciudad_menor_5k))
print (ciudad_menor_5k)


#Filtrar 
s5 = series_valor_ciudad[ciudad_menor_5k]

series_valor_ciudad = series_valor_ciudad * 1.10

series_valor_ciudad["Quito"] = series_valor_ciudad["Quito"] -50 

print ("Lima" in series_valor_ciudad)



for i in valores_ciudad:
    print ("Ciudades",i)





