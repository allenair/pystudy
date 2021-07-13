# -*- coding: utf-8 -*-
from sklearn import datasets

iris_data = datasets.load_iris()
data = iris_data.get('data')
target = iris_data.get('target')
print(data.shape)
print(target.shape)