# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:47:41 2019

@author: dhanu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
#Importing Datasets and setting up working directory 
dataset=pd.read_csv('Data.csv')
#To create a vector with all the independant variables except the dependant variables(purchased)
X=dataset.iloc[:,:-1].values
# To create a vector with dependant variable (purchased) and first index(country) is 0
Y=dataset.iloc[:,3]

# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(
        [('one_hot_encoder', OneHotEncoder(), [0])],
        remainder = 'passthrough')
X = np.array(ct.fit_transform(X), dtype = np.float)
# Encoding the Dependent Variable
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)