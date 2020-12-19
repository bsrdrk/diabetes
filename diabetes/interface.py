# -*- coding: utf-8 -*-
#import libraries
import pickle
import tkinter as tk
import pandas as pd
from tkinter import *
#%% load_model
filename = 'diabetes_model.pkl'
with open(filename, 'rb') as file:
    model = pickle.load(file)

#%%
d = {'Pregnancies':        7.00,
     'Glucose':            106.00,
     'BloodPressure':      92.00,
     'SkinThickness':     18.00,
     'Insulin':           0.00,
     'BMI' :              22.70,
     'DiabetesPedigreeFunction':     0.23,
     'Age':               48.00,}
test_v = pd.Series(d)
test_v = test_v.values.reshape(1,-1)
score = model.predict(test_v)
#%%
def score_checker(score):
    #END = '0.0'
    #Score.get()
    Score.config(state=NORMAL)
    Score.delete("0.0",END)
    
    if score == 0:
        Score.config(state=NORMAL)
        Score.delete("0.0",END)
        Score.insert( END, "Your result is 0")        
    elif score == 1 :
        Score.delete("0.0",END)
        Score.config(state=NORMAL)
        Score.insert(END, "Your result is 1")   
        
    else:
        Score.delete("0.0",END)
        Score.config(state=NORMAL)
        Score.insert(END, "'Please enter your values \n and click Check button',  font=('calibre',10, 'bold'")         
    Score.config(state=DISABLED)
    Score.yview(END)
    
def check():
    val_dict = {'Pregnancies':   Pregnancies_entry.get(),
     'Glucose':           Glucose_entry.get(),
     'BloodPressure':     BloodPreddure_entry.get(),
     'SkinThickness':     SkinThickness_entry.get(),
     'Insulin':           Insulin_entry.get(),
     'BMI' :              BMI_entry.get(),
     'DiabetesPedigreeFunction':    DiabetesPedigreeFunction_entry.get(),
     'Age':               Age_entry.get()}
    test_v = pd.Series(val_dict)
    test_v = test_v.values.reshape(1,-1)
    score = model.predict(test_v) 
    score_checker(score)
def reset():
    Pregnancies.set(0)
    Glucose.set(0)
    BloodPreddure.set(0)
    SkinThickness.set(0)
    Insulin.set(0)
    BMI.set(0)
    DiabetesPedigreeFunction.set(0)
    Age.set(0)
    Score.config(state=NORMAL)
    Score.delete("0.0" , END)
    Score.config(state=DISABLED)
    
#%% 

base = tk.Tk()
Pregnancies = tk.IntVar()        
Glucose = tk.IntVar()
BloodPreddure = tk.IntVar()
SkinThickness=tk.IntVar()
Insulin= tk.IntVar()
BMI   =tk.IntVar()
DiabetesPedigreeFunction=tk.IntVar()
Age = tk.IntVar() 
Score = tk.Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
Score.config(state=tk.DISABLED)
base.title('Diabetes')
base.geometry('400x300')

Pregnancies_label = tk.Label(base, text = 'Pregnancies',  font=('calibre',10, 'bold')) 
Pregnancies_entry = tk.Entry(base, textvariable = Pregnancies, font=('calibre',10,'normal')) 

Glucose_label = tk.Label(base, text = 'Glucose',  font=('calibre',10, 'bold')) 
Glucose_entry = tk.Entry(base, textvariable = Glucose, font=('calibre',10,'normal')) 

BloodPreddure_label = tk.Label(base, text = 'BloodPreddure',  font=('calibre',10, 'bold')) 
BloodPreddure_entry = tk.Entry(base, textvariable = BloodPreddure, font=('calibre',10,'normal')) 

SkinThickness_label = tk.Label(base, text = 'SkinThickness',  font=('calibre',10, 'bold')) 
SkinThickness_entry = tk.Entry(base, textvariable =SkinThickness, font=('calibre',10,'normal')) 

Insulin_label = tk.Label(base, text = 'Insulin',  font=('calibre',10, 'bold')) 
Insulin_entry = tk.Entry(base, textvariable = Insulin, font=('calibre',10,'normal')) 

BMI_label = tk.Label(base, text = 'BMI',  font=('calibre',10, 'bold')) 
BMI_entry = tk.Entry(base, textvariable = BMI, font=('calibre',10,'normal')) 

DiabetesPedigreeFunction_label = tk.Label(base, text = 'DiabetesPedigreeFunction',  font=('calibre',10, 'bold')) 
DiabetesPedigreeFunction_entry = tk.Entry(base, textvariable = DiabetesPedigreeFunction, font=('calibre',10,'normal')) 

Age_label = tk.Label(base, text = 'Age',  font=('calibre',10, 'bold')) 
Age_entry = tk.Entry(base, textvariable = Age, font=('calibre',10,'normal')) 

sub_btn=tk.Button(base,text = 'Check', command = check) 
reset_btn=tk.Button(base,text = 'Reset', command = reset) 
Score_label =tk.Label(base, text = 'Result:',  font=('calibre',10, 'bold')) 

Pregnancies_label.grid(row=0,column=1) 
Pregnancies_entry.grid(row=0,column=2) 

Glucose_label.grid(row=1,column=1) 
Glucose_entry.grid(row=1,column=2) 

BloodPreddure_label.grid(row=2,column=1) 
BloodPreddure_entry.grid(row=2,column=2) 

SkinThickness_label.grid(row=3,column=1) 
SkinThickness_entry.grid(row=3,column=2) 

Insulin_label.grid(row=4,column=1) 
Insulin_entry.grid(row=4,column=2) 

BMI_label.grid(row=5,column=1) 
BMI_entry.grid(row=5,column=2) 

DiabetesPedigreeFunction_label.grid(row=6,column=1) 
DiabetesPedigreeFunction_entry.grid(row=6,column=2) 

Age_label.grid(row=7,column=1) 
Age_entry.grid(row=7,column=2) 

sub_btn.grid(row=8,column=2)
reset_btn.grid(row = 8, column = 3) 
Score_label.place(x = 0 , y = 220)
Score.place(x =0, y=250, height = 30, width = 398)
#Score_enrty.grid(row = 10 , column = 1)
base.mainloop()



