# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:01:37 2020

@author: Ronald
"""

import pandas as pd
import numpy as np
import os

path = "./Data/BostonHousing.csv"

df1 = pd.read_csv(path, nrows=10)

columnas = ['crim','zn', 'indus','chas']

df2 = pd.read_csv(path,nrows=10,usecols=columnas)

##19
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

ser2 =pd.Series(ser,index=[0,4,8,14,20]) 

