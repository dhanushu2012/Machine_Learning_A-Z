# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:28:07 2019

@author: dhanu
"""
##Data Pre-processing 
#Importing Libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
#Importing Datasets and setting up working directory 
dataset=pd.read_csv('Data.csv')
#To create a vector with all the independant variables except the dependant variables(purchased)
X=dataset.iloc[:,:-1].values
# To create a vector with dependant variable (purchased) and first index(country) is 0
Y=dataset.iloc[:,3]
