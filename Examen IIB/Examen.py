# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:10:49 2020

@author: Ronald
"""

import numpy as np
import pandas as pd

#1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros
arr_pand = np.random.randint(10,size=(10,6))
df1 = pd.DataFrame(arr_pand)
s1 = df1.iloc[0]
s2 = df1.iloc[-1]

#2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico
#                  A         B         C         D
#2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
#2013-01-02  1.212112 -0.173215  0.119209 -1.044236
#2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
#2013-01-04  0.721555 -0.706771 -1.039575  0.271860
#2013-01-05 -0.424972  0.567020  0.276232 -1.087401
#2013-01-06 -0.673690  0.113648 -1.478427  0.524988

arr_pand = np.random.randint(10,size=(6,4))
df2 = pd.DataFrame(arr_pand)
df2.index = ['2013-01-01','2013-01-02','2013-01-03','2013-01-04','2013-01-05','2013-01-06']
df2.columns = ['A','B','C','D']
#4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.
arr_pand = np.random.randint(10,size=(10,6))
df4 = pd.DataFrame(arr_pand)
columnas_df4 = df4.columns.values
valores_df4 = df4.values
#5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe
arr_pand = np.random.randint(10,size=(10,6))
df5 = pd.DataFrame(arr_pand)
descripcion_df5 = df5.describe()
#6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos
arr_pand = np.random.randint(10,size=(10,6))
df6 = pd.DataFrame(arr_pand)
df6 = pd.DataFrame(arreglo6)
transpuesto_df6 = df6.transpose()
#7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente
arr_pand = np.random.randint(10,size=(10,6))
df7 = pd.DataFrame(arr_pand)
df7.columns = ['A','B','C','D','E','F']
ordenado = df7.sort_values(['A','B','C','D','E','F'], ascending=False)
ordenado2 = df7.sort_values(['A','B','C','D','E','F'])
#8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7
arreglo1 = np.random.randint(0, 10, 60).reshape(10,6)
df8 = pd.DataFrame(arreglo1)
df81 = df8[df8[:-1] > 6]
print(df8)
print(df81)
#9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.
arr_pand = np.random.randint(10,size=(10,6))
df9 = pd.DataFrame(arr_pand)
mayores_a_3 = df9 > 3
df9_nan = df9[mayores_a_3]
df9_llenos_0 = df9_nan.fillna(0)
#10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio
arr_pand = np.random.randint(10,size=(10,6))
df10 = pd.DataFrame(arr_pand)
media_df10 = df10.mean()
mediana_df10 = df10.median()
promedio_df10 = df10.mean()
#11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe
arreglo11_1 = np.random.randint(1,10,60).reshape(10, 6)
df11_1 = pd.DataFrame(arreglo11_1)
arreglo11_2 = np.random.randint(1,10,60).reshape(10, 6)
df11_2 = pd.DataFrame(arreglo11_2)
df11_final = df11_1.append(df11_2)
#12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.
arr_pand = np.random.randint(10,size=(10,6))
df12 = pd.DataFrame(arr_pand)
df12_final = pd.DataFrame(df12[0] + df12[1])
df12_final[1] = df12[2] + df12[3]
df12_final[2] = df12[4] + df12[5]
#13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna
arr_pand = np.random.randint(10,size=(10,6))
df13 = pd.DataFrame(arr_pand)
for column in df13.columns:
    print("Columna " + str(column))
    print(df13[column].value_counts())
#14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. Crear una nueva columna con el calculo por fila (A * B ) / C
arr_pand = np.random.randint(10,size=(10,3))
df14 = pd.DataFrame(arr_pand,columns = [
        'A',
        'B',
        'C'])
a = df14['A']
b = df14['B']
c = df14['C']
df14[4] = (a * b)/ c