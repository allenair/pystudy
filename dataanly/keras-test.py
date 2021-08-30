import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(len(x_train))
print(len(y_train))

X_Train = x_train.reshape(x_train[0], -1)/255.
print(X_Train)