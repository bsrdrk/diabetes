# -*- coding: utf-8 -*-
#import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import pickle

#%% Read Data and preprocess
data = pd.read_csv('diabetes.csv')
y = data[['Outcome']]
X= data.drop('Outcome' , axis = 1)
X_train ,  X_test,y_train, y_test = train_test_split(X,y,random_state=42 ,test_size = 0.3)
#%% creating model
model = GradientBoostingClassifier().fit(X_train,y_train)
#%%
score = model.score(X_test,y_test)

#%% save model
filename = 'diabetes_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)
    