# -*- coding: utf-8 -*-

"""расчет квадрата пифагора по дате рождения, вывод на экран """


def sqrt_pif(
        date):
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
    print("-", sum(sqrt_pf), "-", date)
    return sqrt_pf


# ---------------------------sqrt_pif(date)--------------------------
# иициализация списка отец мать
d_b = []
# чтение дат
f = open('data_b1.txt')
for line in f:
    s = line[0:10:1]
    d_b.append(s)
f.close()
print("[в,", "э,", "и,", "ф,", "и,", "з,", "у,", "о,", "у]")
i1 = 0
while i1 < len(d_b):
    sqrt_pif(d_b[i1])
    i1 += 1
