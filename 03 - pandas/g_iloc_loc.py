# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 08:00:02 2020

@author: jeffe
"""


import pandas as pd 


path_guardado = 'C://Users//jeffe//Documents//GIT//python//py-collantes-yunga-jefferson-paul//03 - pandas//data//artwork_data.pickle'
df = pd.read_pickle(path_guardado)


#loc
#sirve para 
#primero = df.loc[1035,'artist']
filtrado_horizontal = df.loc[1035]

print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index)#indices columnas 

serie_vertical = df['artist']

print (serie_vertical)
print(serie_vertical.index)

#filtrar por indice

df_1035 = df[df.index==1035]

segundo = df.loc[1035]#filtrar por indice 
segundo = df.loc[[1035,1036]]#Filtrar por array
segundo = df.loc[3:5]#Filtrar desde un indice x hasta un indice y 

segundo = df.loc[1035,'artist']#1 indice
segundo = df.loc[1035,['artist','medium']]#varios indices

#iloc
tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[df.index == 1035]

tercero = df.iloc[0:10,0:4]


##########
datos = {
    "nota 1":{
        "Pepito":7,
        "Juanita":8,
        "Maria":9},
    "nota 2":{
        "Pepito":7,
        "Juanita":8,
        "Maria":9},
    "disciplina":{
        "Pepito":4,
        "Juanita":9,
        "Maria":2}}

notas = pd.DataFrame(datos)

condicion_nota = notas["nota 1"] > 7
condicion_nota_dos = notas["nota 2"] > 7
condicion_disc = notas["disciplina"] > 7 

mayores_siete = notas.loc[condicion_nota,["nota 1"]]

pasaron = notas.loc[condicion_nota][condicion_nota_dos][condicion_disc]

notas.loc["Maria","disciplina"] = 7

#poner los registros de todas con 7 
notas.loc[:,"disciplina"]=7

#sumar las noras de los registros y dividir para 3 
suma_notas = notas["nota 1"] + notas["nota 2"] +notas["disciplina"]

dividir_notas = suma_notas /3









