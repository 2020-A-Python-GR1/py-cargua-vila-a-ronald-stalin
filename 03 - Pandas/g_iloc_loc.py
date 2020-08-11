# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:10 2020

@author: Ronald
"""

import pandas as pd

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

# loc

filtrado_horizontal = df.loc[1035] # Serie
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index) # Indices columnas

serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index) # Indices son los Indices

print(df['artist'])

# Filtrado por indece
df_1035 = df[df.index == 1035]

# loc -> acceder grupo filas y columnas x LABEL(ARR TRUE AND FALSE)
segundo = df.loc[1035] # Filtrar por indice(1)
segundo = df.loc[[1035,1036]] # Filtrar por arr indices
segundo = df.loc[3:5] # FIltrado desde x indice hasta y indice
segundo = df.loc[df.index == 1035] # Filtrar  por Arreglo -> True False

segundo = df.loc[1035,'artist']
segundo = df.loc[1035,['artist','medium']]

# print(df.loc[0]) # Indice dentro del DataFrame
# print(df[0]) # Indice dentro del DataFrame

tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]

tercero = df.iloc[0:10, 0:4] # Filtrado indices por rando de indice 0:4






