# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EK4WJjQ184JCX1eizuxu1ovTxi17AlzE
"""

# Iimport pandas
import pandas as pd
import numpy as np

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# memuat data
data = pd.read_csv('Car_sales.csv')
for col in data.columns:
  data[col]=data[col].fillna(data[col].mode()[0])
data.head()

data = data.drop(['Manufacturer','Model','Latest_Launch','Vehicle_type'], axis=1)

data.head()

X = data.iloc[:,1:11]  #independent columns
y = data.iloc[:,0]    #target column i.e price range

y=y.round()

bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns)

# menggabungkan 2 dataframe
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Attributes','Score']  #naming the dataframe columns
print(featureScores.nlargest(10,'Score'))

# import library
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

# melakukan ExtraTreesClassifier untuk mengekstraksi fitur
model = ExtraTreesClassifier()
model.fit(X,y)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers

# melakukan plot dari feature importances
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(20).plot(kind='barh')
plt.show()

# mendapatkan  correlations dari setiap fitur dalam dataset
corrmat = data.corr()
top_corr_features = corrmat.index
import seaborn as sns

# plot heatmap
plt.figure(figsize=(11,11))
g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")

"""Dari heatmap diatas,dapat disimpulkan.Bahwa fuel efficieny cenderung berbanding terbalik dengan mayoritas atribut.
Horse power dan engine size  berbanding lurus dengan power_perf_factor."""