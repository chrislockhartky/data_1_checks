# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:45:31 2023

@author: chris
"""
#A program that shows the relationship between zipcodes and Health Code scores in Louisville
#Run the program in Spyder and make sure to have the panes tab open.
#
import pandas as pd
import seaborn as sns
df=pd.read_csv('assets/LouisvilleHealthScores.csv')
sns.scatterplot(data=df, x=df['Zip'], y=df['score'])
