#https://www.hackerrank.com/challenges/predicting-office-space-price/problem
"""
Input Format
The first line contains two space separated integers, F and N. Over here, F is the number of observed features. N is the number of rows for which features as well as price per square-foot have been noted. 
This is followed by a table having F+1 columns and N rows with each row in a new line and each column separated by a single space. The last column is the price per square foot.
The table is immediately followed by integer T followed by T rows containing F columns.

2 4
0.44 0.68 511.14
0.99 0.23 717.1
0.84 0.29 607.91
0.28 0.45 270.4
4
0.05 0.54
0.91 0.91
0.31 0.76
0.51 0.31
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn import linear_model as lm
from sklearn import preprocessing as pp

F, N = map(int, input().split())
train = np.array([input().split() for _ in range(N)], float)
T=int(input())
test=np.array([input().split() for _ in range(T)],float)

train_features=train[:,:-1]
train_label=train[:,-1]

model=lm.LinearRegression()
features=pp.PolynomialFeatures(3,include_bias=False) #polynomial regression as per required
model.fit(features.fit_transform(train_features),train_label)
predictions=model.predict(features.transform(test))

#unpack and print
print(*predictions, sep='\n')


