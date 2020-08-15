# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:29:51 2020

@author: jeffe
"""


import pandas as pd
import numpy as np
import os
import sqlite3



df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()
 
path_excel = 'C://Users//jeffe//Documents//GIT//python//py-collantes-yunga-jefferson-paul//03 - pandas//data//artwork_data.xlsx'
path_excel_indice = 'C://Users//jeffe//Documents//GIT//python//py-collantes-yunga-jefferson-paul//03 - pandas//data//artwork_data_indice.xlsx'
path_excel_columnas = 'C://Users//jeffe//Documents//GIT//python//py-collantes-yunga-jefferson-paul//03 - pandas//data//artwork_data_columnas.xlsx'

#Guardar el exccel con indice 
#sub_df.to_excel(path_excel)

#sin indice
#sub_df.to_excel(path_excel_indice, index = False)

columnas = ['artist','title','year']

sub_df.to_excel(path_excel_columnas,columns = columnas)


#Multiples hojas de trabajo

#path_excel_mt = 'C://Users//jeffe//Documents//GIT//python//py-collantes-yunga-jefferson-paul//03 - pandas//data//artwork_data_mt.xlsx'

writer = pd.ExcelWriter(path_excel_mt,engine='xlsxwriter')

sub_df.to_excel(writer,sheet_name = 'Primera')
sub_df.to_excel(writer,sheet_name = 'Segunda')
sub_df.to_excel(writer,sheet_name = 'Tercera')
writer.save()

#Formato condicional 

num_artista = sub_df['artist'].value_counts()
path_excel_colores = 'C://Users//jeffe//Documents//GIT//python//py-collantes-yunga-jefferson-paul//03 - pandas//data//artwork_data_colores.xlsx'

writer = pd.ExcelWriter(path_excel_colores,engine = 'xlsxwriter')

num_artista.to_excel(writer,sheet_name='Artistas')

hoja_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artista.index)+1)

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)

writer.save()


###SQL####
with sqlite3.connect("bdd_artist.bdd") as conexion: sub_df.to_sql('py_artistas',conexion)

###JSON###
sub_df.to_json('artistas.json')
sub_df.to_json('artista_tabla.json',orient = 'table')





