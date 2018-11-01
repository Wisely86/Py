#!/usr/bin/env python 
# -*- coding:utf-8 -*-
age = 32
if age >= 18:
    print("age1",age)
elif age < 20:
    print("age2",age)
elif age >= 30:
    print("age3",age)
else:
    print("aaa")

x = "wisely"
if x:
    print("只要x是非零数值、非空字符串、非空list等，判断为True，打印此行")
else:
    print("只要x是零数值、空字符串、空list等，判断为False，打印此行")

#input()返回的数据类型是str，str不能直接和整数比较，必须先把str使用int()转换成整数
birth = input('birth: ')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')


name = input('name: ')
if name == "wisely":
    print("YES")
else:
    print("NO")
