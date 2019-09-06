#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:57:35 2019

@author: Mx
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing data
data = pd.read_csv('/home/Mx/M_L/A-Z/datas/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/Data_Preprocessing/Data.csv')
X = data.iloc[:,:-1].values  # : we take all lines except last. because last is dependent var   .values is we are taking all the values

X

y = data.iloc[:,3].values  #taking last column

y

from sklearn.preprocessing import Imputer  #imputer class

imputer = Imputer(missing_values='NaN', strategy = 'mean', axis=0)  #axis= 0 gives mean of column

imputer = imputer.fit(X[:,1:3])

X[:, 1:3]= imputer.transform(X[:,1:3])

from sklearn.preprocessing import LabelEncoder  #class from sklearn
labelencoder_X = LabelEncoder()                 #creating obj to encode
X[:,0] = labelencoder_X.fit_transform(X[:,0])            #applying fit transform method in X  apply in 1st column


from sklearn.preprocessing import LabelEncoder  #class from sklearn
labelencoder_X = LabelEncoder()                 #creating obj to encode
X[:,0] = labelencoder_X.fit_transform(X[:,0])            #applying fit transform method in X  apply in 1st column


from sklearn.preprocessing import LabelEncoder, OneHotEncoder  #class from sklearn
labelencoder_X = LabelEncoder()                 #creating obj to encode
X[:,0] = labelencoder_X.fit_transform(X[:,0])            #applying fit transform method in X  apply in 1st column
onehotencoder = OneHotEncoder(categorical_features =[0])
X = onehotencoder.fit_transform(X).toarray()


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0]) 
onehotencoder = OneHotEncoder(categorical_features =[0])
X = onehotencoder.fit_transform(X).toarray()




labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y) 


from sklearn.model_selection import train_test_split
X_train, X_test , y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()  #creating obj
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

