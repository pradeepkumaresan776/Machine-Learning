"""
Created on Sat Sep  2 11:11:13 2023

@author: Pradeep
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
df = pd.read_csv('/home/python/Documents/project/Salary prediction/ML/salary_pred/purhchase_data.csv')
df = df.replace({'Gender':{'Male':1, 'Female':0}})
df.head()
x = df.iloc[:, [1, 2, 3]]
y = df.iloc[:, 4]
# Train and Test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)
# Scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
# Moding
model = RandomForestClassifier(n_estimators=10)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
# find accuracy score
acc = metrics.accuracy_score(y_test, y_pred)
print(acc)
def find_pred(gender, age, salary):
    x = [[gender, age, salary]]
    test_x = sc.transform(x)
    y_pred = model.predict(test_x)
    return y_pred

'''
cm = metrics.confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8,6))
plt.title("Model accuracy")
plt.xlabel('y pred value')
plt.ylabel('y test value')
sbn.heatmap(cm, cmap='Blues', annot=True)
plt.show()
'''



































