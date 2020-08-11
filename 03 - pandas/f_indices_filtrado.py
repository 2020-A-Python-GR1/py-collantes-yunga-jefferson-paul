# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:34:12 2020

@author: jeffe
"""




import pandas as pd

path_guardado = 'C://Users//jeffe//Documents//GIT//python//py-collantes-yunga-jefferson-paul//03 - pandas//data//artwork_data.pickle'
df = pd.read_pickle(path_guardado)


serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)


print(type(artistas)) # Numpy Array

print(artistas.size)
print(len(artistas))
#Filtrar artistas
blake = df['artist'] == 'Blake, William' # Serie
#imprimir el numero de veces que aparece el artista
print(blake.value_counts())

df_blake = df[blake] # DataFrame

df_1035 = df[df.index==1035]