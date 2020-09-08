# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:56:14 2020

@author: jeffe
"""


import pandas as pd
import math
import numpy as np


path_guardado = 'C://Users//jeffe//Documents//GIT//python//py-collantes-yunga-jefferson-paul//03 - pandas//data//artwork_data.pickle'

df = pd.read_pickle(path_guardado)


seccion_df = df.iloc[49980:50019,:].copy()

df_agrupar_artista = seccion_df.groupby('artist')

for columna, df_agrupado in df_agrupar_artista:
    print(type(columna))
    print(columna)
    print(type(df_agrupado))
    print(df_agrupado)
    
    
#hacer calculos en columnas del df   
a = seccion_df['units'].value_counts()
# .empty servira para verficar si la columna esta vacia
print(a.empty)

def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    if (lista_valores.empty == True):
        return series
    else:
        if (tipo == 'promedio'):
            suma = 0
            numeros_valores = 0
            for valor_serie in series:
                if (isinstance(valor_serie,str)):
                    valor = int (valor_serie)
                    numeros_valores = numeros_valores +1 
                    suma = suma + valor
                else:
                    pass
            promedio = suma / numeros_valores
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
        if (tipo == 'mas_repetido'):
            valores_m_repetidos = series.value_counts().iloc[0]
            series_valores_llenos = series.fillna(valores_m_repetidos)
            return series_valores_llenos
        
        

            
            
            
            
def transformar_df (df):
    df_artist = df.groupby('artist')
    lista_df = []
    for artista, df in df_artist:
        copia_df = df.copy()
        
        serie_w = copia_df['width']
        serie_h = copia_df['height']
        serie_u = copia_df['units']
        serie_i = copia_df['title']
        copia_df.loc[:,'width'] = llenar_valores_vacios(serie_w,'promedio')
        copia_df.loc[:,'height'] = llenar_valores_vacios(serie_h,'promedio')
        copia_df.loc[:,'units'] = llenar_valores_vacios(serie_u,'mas_repetido')
        copia_df.loc[:,'title'] = llenar_valores_vacios(serie_i,'mas_repetido')
        lista_df.append(copia_df)
    df_completo = pd.concat(lista_df)
    return df_completo
df_lleno = transformar_df(seccion_df)
        