# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt
import itertools

"""поиск родственников исходя из уменьшения ошибки при обучении нейросети """


# функция для обучения нейросети
def nonlin(
        x, deriv=False):
            if (deriv is True):
                return x * (1 - x)
            return (1 / (1 + np.exp(-x)))


# функция для вычисления качеств квадрата пифагора
def sqrt_pif(
        date, name):
    # подсчет рабочих цифр для квадрата
    # print("-------------",date,"-----------------")
    s1 = date.replace(".", "")
    # print(s1[1])
    wd1 = 0
    i = 0
    while i < len(s1):
        wd1 = wd1 + int(s1[i])
        i = i + 1
    # print("первое рабочее число",wd1)
    wd2 = 0
    s2 = str(wd1)
    i = 0
    while i < len(s2):
        wd2 = wd2 + int(s2[i])
        i = i + 1
    # print("второе рабочее число",wd2)
    s_sp = s1.split(".")
    if s1[0] == '0':
        wd3 = wd1 - (2 * int(s1[1]))
    else:
        wd3 = wd1 - (2 * int(s1[0]))
    # print("третье рабочее число",wd3)
    wd4 = 0
    i = 0
    while i < len(str(wd3)):
        wd4 = wd4 + int(str(wd3)[i])
        i = i + 1
    # print("четвертое рабочее число", wd4)
    # печать квадрата в виде списка где указано количество вхождений
    # качества на соответствующей позиции
    s1 = s1 + str(wd1) + str(wd2) + str(wd3) + str(wd4)
    sqrt_pf = []
    i = 1
    while i < 10:
        sqrt_pf.append(s1.count(str(i)))
        i += 1
    print(sqrt_pf, end = '')
    print("-", sum(sqrt_pf), "-", date, "-", name)
    return sqrt_pf


def determ_relationship(
             X, y, Wt, St):
    # нормализация перед вычислениями
    X_norm = 2 * np.random.random((9, 3)) + 1
    j = 0
    i = 0
    while i < 9:
        while j < 3:
            X_norm[i, j] = (((X[i, j] - 0) * (1 - 0)) / (Wt - 0) + 0)
            j += 1
        j = 0
        i += 1

    # print("Входные данные:")
    # print(X.T)
    X = X_norm

    # Результат
    # print("К такому результату стремимся в обучении:")
    # print(y.T)

    y_norm = 2 * np.random.random((9, 1)) + 1
    i = 0
    while i < 9:
            y_norm[i] = (((y[i] - 0) * (1 - 0)) / (Wt - 0) + 0)
            i += 1
    y = y_norm

    # случайный выбор становится определенным - требуется на этапе разработке
    np.random.seed(1)

    # случайно инициализируем веса, в среднем - 0
    syn0 = 2 * np.random.random((3, 9)) - 1
    syn1 = 2 * np.random.random((9, 1)) - 1

    # инициализация массивов для графического представления

    l2_er_gr = []
    f_num = []

    for j in range(St):
        # проходим слои 0, 1 и 2
        # для данных обучения
        l0 = X
        l1 = nonlin(np.dot(l0, syn0))
        l2 = nonlin(np.dot(l1, syn1))

        # вычисление ошибки
        l2_error = y - l2

        # наполняем массивы для графиков ошибок
        l2_er_gr.append(np.mean(np.abs(l2_error)))
        f_num.append(j)

        l2_delta = l2_error * nonlin(l2, deriv=True)

        # как сильно значения l1 влияют на ошибки в l2?
        l1_error = l2_delta.dot(syn1.T)

        # в каком направлении нужно двигаться, чтобы прийти к l1?
        # если мы были уверены в предсказании, то сильно менять его не надо
        l1_delta = l1_error * nonlin(l1, deriv=True)

        syn1 += l1.T.dot(l2_delta)
        syn0 += l0.T.dot(l1_delta)

    # print ("Вывод после обучения:")
    # i = 0
    # while i < 9:
    #         y_norm[i] = l2[i] * Wt
    #         i += 1
    # Z = y_norm.T
    # Z = (np.rint(y_norm)).T
    # print(Z)

    er_learn = str(np.mean(np.abs(l2_error)))

    # итоговые ошибки
    print("er_learn", er_learn)
    my_file.write(er_learn)
    my_file.write(' ,')
    return(er_learn)

# ---------------------------начало вычислений--------------------------
# чтение файла с датами рождения и именами
d_b = []
date_name = []
# чтение дат
f = open('birthday_base.txt')
for line in f:
    date_ = line[0:10:1]
    name_ = line[11:-1]
    date_name.append(date_)
    date_name.append(name_)
    d_b.append(date_name)
    date_name = []
f.close()

# обсчет прочитанных данных из файла, вывод квадрата,
# базы списками из квадрата, даты, номера, имени
date_name = []
sqrt_name = []  # база из списков квадрат, дата, номер, имя
i1 = 0
while i1 < len(d_b):
    print(i1, " ", end = '')
    date_name.append(sqrt_pif(d_b[i1][0], d_b[i1][1]))
    date_name.append(d_b[i1][0])
    date_name.append(i1)
    date_name.append(d_b[i1][1])
    sqrt_name.append(date_name)
    date_name = []
    i1 += 1

print("всего записей", i1)

# ----формирование списка всех комбинаций из номеров людей в базе-------------
combo_source = [k for k in range(0, i1)]
combo_list = (list(itertools.permutations(combo_source, 4)))

print(len(combo_list))


# --------------------данные для обучения нейросети---------------------------
Wt_ = 5   # вес для нормальизации - макс. значение качества в ячейке квадрата
St_ = 120  # количество проходов в обучении нейросети


my_file = open("results.txt", "w")
# len(combo_list)/2

w = 0
while w < (len(combo_list)):
    source_d = combo_list[w]
    # человек 1, 2, 3
    Set1 = np.array([sqrt_name[source_d[0]][0],
                     sqrt_name[source_d[1]][0],
                     sqrt_name[source_d[2]][0]])
    # человек - результат
    Hum1 = np.array([sqrt_name[source_d[3]][0]]).T
    Set1 = Set1.T
    determ_relationship(Set1, Hum1, Wt_, St_)
    my_file.write(sqrt_name[source_d[0]][3])
    my_file.write(',')
    my_file.write(sqrt_name[source_d[1]][3])
    my_file.write(',')
    my_file.write(sqrt_name[source_d[2]][3])
    my_file.write(',')
    my_file.write(sqrt_name[source_d[3]][3])
    my_file.write('\n')
    w += 1

# source_d = [0, 1, 3, 4]
# Set1 = np.array([sqrt_name[source_d[0]][0],
#                  sqrt_name[source_d[1]][0],
#                  sqrt_name[source_d[2]][0]])
# # человек - результат
# Hum1 = np.array([sqrt_name[source_d[3]][0]]).T
# Set1 = Set1.T

# determ_relationship(Set1, Hum1, Wt_, St_)

# print(Set1)
# print(Hum1)

my_file.close()
# plt.title('Errors graph')
# plt.plot(f_num, l2_er_gr)
# plt.xlabel('f_num')
# plt.ylabel('errors')
# plt.show()
