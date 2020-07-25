# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:46:55 2020

@author: jeffe
"""




import numpy as np
import pandas as pd 

arr_pand = np.random.randint(0,10,6).reshape(2,3)
#cuando se genera el dataFrame se genera los indices
df1 = pd.DataFrame(arr_pand)
#para agarra una columna(serie)
s1 = df1[0]

s2 = df1[1]

s2 = df1[2]

df1[3] = s1

#realizar una operacion entre seriesque estan dentro del dataFrame
df1[4] = s1 *s2



datos_fisicos_uno = pd.DataFrame(arr_pand,
                                 columns=['Estatura(cm)','Peso(kg)','Edad(anios)'])



datos_fisicos_dos = pd.DataFrame(arr_pand,
                                 columns=['Estatura(cm)','Peso(kg)','Edad(anios)'],
                                 index=['Jefferson','Paul'])

serie_peso = datos_fisicos_dos['Peso(kg)']
datosJefferson = serie_peso['Jefferson']

print(datosJefferson)


#//modificar los indices
df1.index=['Paul', 'Jefferson']
df1.index=['Manuel','Pedro']
df1.columns = ['A','B','C','D','E'] 



















