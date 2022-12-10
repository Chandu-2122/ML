# -*- coding: utf-8 -*-
"""AI_Major

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nwpP8z0P0aw4g5r0TvwF7VJ2O7is21rT
"""

import pandas as pd
df = pd.read_csv('/content/wine.csv')
df

df['quality'] = df['quality'].map({'bad':0,'good':1})
df

df.isnull().sum()

df.describe()

df.info()

#since there are no null values lets divide the data into input and output
#input-fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol
#output-quality ('good' and 'bad' based on score >5 and <5)
x = df.iloc[:,0:6].values
x

y = df.iloc[:,11].values
y

#running the classifier
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

#fit the model
model.fit(x,y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state = 0)
x_train.shape
x_test.shape

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
y_pred

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_pred, y_test)*100

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

sns.barplot('quality', 'fixed acidity', data = df)

sns.barplot('quality', 'volatile acidity', data = df)

sns.barplot('quality', 'citric acid', data = df)

sns.barplot('quality', 'residual sugar', data = df)

sns.barplot('quality', 'chlorides', data = df)

sns.barplot('quality', 'free sulfur dioxide', data = df)

sns.barplot('quality', 'total sulfur dioxide', data = df)

sns.barplot('quality', 'density', data = df)

sns.barplot('quality', 'pH', data = df)

sns.barplot('quality', 'sulphates', data = df)

sns.barplot('quality', 'alcohol', data = df)

df

x = df.iloc[:,0:4].values
x

y = df.iloc[:,6].values
y

'''df.drop(['pH'],axis=1,inplace=True)
df.drop(['alcohol'],axis=1,inplace=True)
df.drop(['density'],axis=1,inplace=True)
df.drop(['residual sugar'],axis=1,inplace=True)
df.drop(['fixed acidity'],axis=1,inplace=True)'''

model.fit(x,y)

x_train, x_test, y_train, y_test = train_test_split(x,y,random_state = 0)
x_train.shape
x_test.shape

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
y_pred

accuracy_score(y_pred, y_test)*100

from scipy import stats
import numpy as np
df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

sns.pairplot(df)



x = df.iloc[:,0:11].values
x

y = df.iloc[:,11].values
y

x_train, x_test, y_train, y_test = train_test_split(x,y,random_state = 0)
x_train.shape
x_test.shape

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
y_pred

accuracy_score(y_pred, y_test)*100

