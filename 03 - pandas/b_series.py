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

svc_cuadrado = np.square(series_valor_ciudad)


ciudades_uno = pd.Series({
    "Montanita" : 3000,
    "Guayaquil" : 10000,
    "Quito" : 2000})

ciudades_dos = pd.Series({
    "Loja" : 300,
    "Guayaquil":100000})

ciudades_uno["Loja"] = 10
#se puede multiplicar, restar y dividir 
print (ciudades_uno + ciudades_dos)

ciudades_add = ciudades_uno.add(ciudades_dos)

ciu_concat = pd.concat([ciudades_uno,ciudades_dos])
#para verificar que dos series sean iguales
ciu_concat_verify = pd.concat([
    ciudades_uno,
    ciudades_dos],
    verify_integrity=False)

ciu_append_verify = ciudades_uno.append(
    ciudades_dos,
    verify_integrity=False)

print(ciudades_uno.max())
print (pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))

print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))

print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))

#Sacar las primeros o ultimos elementos de la serie
print (ciudades_uno.head(2))
print(ciudades_uno.tail(2))

print(ciudades_uno.sort_values(ascending = False).head(2))

print(ciudades_uno.sort_values().tail(2))

#0 - 10000 5%
#1001 - 5000 10%
#5001 - 20000 15%
def calcular (valor_serie):
    if (valor_serie <= 1000):
        return valor_serie * 1.05
    if (valor_serie > 1000 and valor_serie <= 5000):
        return valor_serie * 1.10
    if (valor_serie > 5000):
        return valor_serie * 1.15
ciudad_calculada = ciudades_uno.map(calcular)

# if else 
# Cuando no se cumple la condicion se aplica la formula 
resultado = ciudades_uno.where(ciudades_uno < 1000,
                   ciudades_uno * 1.05)


#posibles problemas que se puede tener 
series_numeros = pd.Series(['1.0','2',-3])
print(pd.to_numeric(series_numeros))
#para definir que tipo de datos quremos (integer, signed, unsigned,float)
print (pd.to_numeric(series_numeros, downcast='integer'))

series_numeros_err = pd.Series(['no tiene madre','1.0','2',-3])

# ignore para ignorar lo errores, coerce, riase(DEafult)
#print(pd.to_numeric(series_numeros_err))
print(pd.to_numeric(series_numeros_err,errors='ignore'))
print(pd.to_numeric(series_numeros_err,errors='coerce'))


























