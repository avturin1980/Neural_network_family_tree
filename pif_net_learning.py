# -*- coding: utf-8 -*-
import numpy as np

"""Программа обучает нейросеть на данных квадрата пифгора"""


def nonlin(
        x, deriv=False):
            if (deriv is True):
                return x * (1 - x)
            return (1 / (1 + np.exp(-x)))


X = np.array([[4, 4, 2],
              [4, 0, 3],
              [0, 2, 0],
              [2, 1, 3],
              [0, 0, 0],
              [1, 2, 1],
              [1, 0, 0],
              [1, 2, 2],
              [1, 3, 1]])

X_norm = 2 * np.random.random((9, 3)) + 1
j = 0
i = 0
while i < 9:
    while j < 3:
        X_norm[i, j] = (((X[i, j] - 0) * (1 - 0)) / (5 - 0) + 0)
        j += 1
    j = 0
    i += 1

print("Входные данные:")
print(X)
X = X_norm

# Результат
y = np.array([[2, 4, 0, 1, 0, 1, 2, 1, 1]]).T
y_norm = 2 * np.random.random((9, 1)) + 1
i = 0
while i < 9:
        y_norm[i] = (((y[i] - 0) * (1 - 0)) / (5 - 0) + 0)
        i += 1
y = y_norm

# случайный выбор становится определенным
np.random.seed(1000)

# случайно инициализируем веса, в среднем - 0
syn0 = 2 * np.random.random((3, 9)) - 1
syn1 = 2 * np.random.random((9, 1)) - 1
print(syn0)
print(syn1)

for j in range(60000):
    # проходим вперёд по слоям 0, 1 и 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # как сильно мы ошиблись относительно нужной величины?
    l2_error = y - l2

    if (j % 10000) == 0:
        print ("Error:" + str(np.mean(np.abs(l2_error))))

    # в какую сторону нужно двигаться?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l2_delta = l2_error * nonlin(l2, deriv=True)

    # как сильно значения l1 влияют на ошибки в l2?
    l1_error = l2_delta.dot(syn1.T)

    # в каком направлении нужно двигаться, чтобы прийти к l1?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)


print ("Выходные данные после тренировки:")
i = 0
while i < 9:
        y_norm[i] = l2[i] * 5
        i += 1
Z = (np.rint(y_norm)).T
print(Z)
