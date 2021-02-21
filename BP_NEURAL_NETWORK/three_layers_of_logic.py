import numpy as np
from PyQt5.QtWidgets import QApplication,QWidget

X = np.array([[1, 0, 0],
              [1, 0, 1],
              [0, 1, 0],
              [1, 1, 1]])

Y = np.array([[0, 1, 1, 0]])

V = np.random.random((3, 4)) * 2 - 1
W = np.random.random((4, 1)) * 2 - 1

lr = 0.11


def sigmoid(X):
    return 1 / (1 + np.exp(-X))


def dsigmiod(X):
    return X * (1 - X)


def update():
    global X, Y, V, W, lr
    L1 = sigmoid(np.dot(X, V))
    L2 = sigmoid(np.dot(L1, W))

    L2_delta = (Y.T - L2) * dsigmiod(L2)
    L1_delta = L2_delta.dot(W.T) * dsigmiod(L1)

    W_C = lr * L1.T.dot(L2_delta)
    V_C = lr * X.T.dot(L1_delta)

    W = W + W_C
    V = V + V_C


for i in range(30000):
    update()
    if i % 500 == 0:
        L1 = sigmoid(np.dot(X, V))
        L2 = sigmoid(np.dot(L1, W))
        print('ERROR:', np.mean(np.abs(Y.T - L2)))

L1 = sigmoid(np.dot(X, V))
L2 = sigmoid(np.dot(L1, W))
print(L1,L2)
