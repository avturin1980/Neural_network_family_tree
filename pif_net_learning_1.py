# -*- coding: utf-8 -*-
import numpy as np

"""Программа обучает нейросеть на данных квадрата пифгора"""


def nonlin(
        x, deriv=False):
            if (deriv is True):
                return x * (1 - x)
            return (1 / (1 + np.exp(-x)))


# # 1 2 3
# X = np.array([[4, 4, 0, 2, 0, 1, 1, 1, 1],
#               [2, 0, 2, 2, 0, 3, 1, 0, 3],
#               [3, 5, 1, 1, 0, 1, 1, 1, 1]])
# # 4
# y = np.array([[2, 3, 0, 3, 0, 1, 0, 2, 1]]).T

# # 4 5 6
# X = np.array([[2, 3, 0, 3, 0, 1, 0, 2, 1],
#               [3, 2, 3, 1, 0, 2, 0, 1, 2],
#               [1, 2, 3, 1, 1, 0, 2, 1, 1]])
# # 7
# y = np.array([[5, 1, 0, 0, 2, 1, 2, 1, 0]]).T

# # 8 9 10
# X = np.array([[1, 2, 3, 1, 1, 0, 2, 1, 1],
#               [1, 3, 1, 1, 3, 2, 0, 0, 1],
#               [5, 1, 3, 0, 0, 0, 0, 1, 2]])
# # 5
# y = np.array([[3, 2, 3, 1, 0, 2, 0, 1, 2]]).T

# 
X = np.array([[6, 2, 1, 0, 1, 1, 0, 0, 2],
              [5, 3, 1, 0, 1, 0, 1, 1, 1],
              [5, 2, 1, 2, 0, 0, 2, 0, 2]])
# 
y = np.array([[2, 0, 2, 2, 0, 3, 1, 0, 3]]).T

X = X.T

# нормализация перед вычислениями
X_norm = 2 * np.random.random((9, 3)) + 1
j = 0
i = 0
while i < 9:
    while j < 3:
        X_norm[i, j] = (((X[i, j] - 0) * (1 - 0)) / (6 - 0) + 0)
        j += 1
    j = 0
    i += 1

print("Входные данные:")
print(X)
X = X_norm

# Результат
print("Прогнозируемый результат:")
print(y.T)

y_norm = 2 * np.random.random((9, 1)) + 1
i = 0
while i < 9:
        y_norm[i] = (((y[i] - 0) * (1 - 0)) / (6 - 0) + 0)
        i += 1
y = y_norm

# случайный выбор становится определенным
np.random.seed(1)

# случайно инициализируем веса, в среднем - 0
syn0 = 2 * np.random.random((3, 9)) - 1
syn1 = 2 * np.random.random((9, 1)) - 1
print(syn0)
print(syn1)

for j in range(900000):
    # проходим слои 0, 1 и 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # вычисление ошибки
    l2_error = y - l2

    if (j % 1000) == 0:
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


print ("Вывод после обучения:")
i = 0
while i < 9:
        y_norm[i] = l2[i] * 6
        i += 1
Z = y_norm.T
print(Z)
Z = (np.rint(y_norm)).T
print(Z)
