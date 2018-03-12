# -*- coding: utf-8 -*-
"""расчет квадрата пифагора по дате рождения, вывод на экран """

def sqrt_pif(date):
    #подсчет рабочих цифр для квадрата
    print("-------------",date,"-----------------")
    s1=date.replace(".","")
    #print(s1[1])
    wd1=0
    i=0
    while i<len(s1):
        wd1=wd1+int(s1[i])
        i=i+1
    #print("первое рабочее число",wd1)
    wd2=0
    s2=str(wd1)
    i=0
    while i<len(s2):
        wd2=wd2+int(s2[i])
        i=i+1
    #print("второе рабочее число",wd2)
    s_sp=s1.split(".")
    if s1[0]=='0':
        wd3=wd1-(2*int(s1[1]))
    else:
        wd3=wd1-(2*int(s1[0]))
    #print("третье рабочее число",wd3)
    wd4=0
    i=0
    while i<len(str(wd3)):
        wd4=wd4+int(str(wd3)[i])
        i=i+1
    #print("четвертое рабочее число",wd4)

    #печать квадрата в виде списка где указано количество вхождений качества на соответствующей позиции
    s1=s1+str(wd1)+str(wd2)+str(wd3)+str(wd4)
    sqrt_pf=[]
    i=1
    while i<10:
        sqrt_pf.append(s1.count(str(i)))
        i+=1
    #print(sqrt_pf,end='')
    #print("-",sum(sqrt_pf),"-",date)

    #печать квадрата в привычной форме сначала в строчку, потом матрицей
    sqrt_l=[]
    i=1
    while i<10:
        j=sqrt_pf[i-1]
        dz=''
        k=0
        while k<j:
            dz=dz+str(i)
            k+=1
        sqrt_l.append(dz)
        i+=1
    #print(sqrt_l)

    seq=[0,3,6,1,4,7,2,5,8]
    i=0
    f=0
    flag=0
    while i<9:
        l=len(sqrt_l[seq[i]])
        k=1
        if l==0:
            print("no", end='')
            flag=1
        else:
            print(sqrt_l[seq[i]], end='')
        if flag==1:
            k=3
        while k<(6-l):
            print(" ", end='')
            k+=1
        f+=1
        if f==3:
            print("")
            f=0
        i+=1
        flag=0
    return sqrt_pf
#---------------------------sqrt_pif(date)--------------------------

d_b=[] #иициализация списка отец мать
#чтение дат
f=open('data_b1.txt')
for line in f:
    s=line[0:10:1]
    d_b.append(s)   
f.close()
print("[в,","э,","и,","ф,","и,","з,","у,","о,","у]")
i1=0
while i1<len(d_b):
    sqrt_pif(d_b[i1])
    i1+=1
    
##sqrt_pif("31.10.1930")
##sqrt_pif("23.04.1931")
##sqrt_pif("23.04.1963")


