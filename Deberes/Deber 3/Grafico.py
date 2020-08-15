# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:03:18 2020

@author: jeffe
"""


import pandas as pd
import numpy as np
import os
import sqlite3
import xlsxwriter

path_guardado = 'C://Users//jeffe//Documents//GIT//python//py-collantes-yunga-jefferson-paul//03 - pandas//data//artwork_data.pickle'

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()
num_artista = sub_df['artist'].value_counts()
rango_celdas = 'B2:B{}'.format(len(num_artista.index)+1)


workbook = xlsxwriter.Workbook('grafico.xlsx')
worksheet = workbook.add_worksheet()



chart = workbook.add_chart({'type': 'column'})


chart.add_series({		
    'categories': '=Sheet1!$A$2:$A${}'.format(len(num_artista.index)+1),
    				
    'values':     '=Sheet1!$B$2:$B${}'.format(len(num_artista.index)+1),
})

chart.set_title ({'name': 'Artists '})
chart.set_x_axis({'name': 'Artist'})
chart.set_y_axis({'name': 'N'})

chart.set_style(11)

worksheet.insert_chart('D2', chart, {'x_offset': 25, 'y_offset': 10})

workbook.close()