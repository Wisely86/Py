#!/usr/bin/env python 
# -*- coding:utf-8 -*-
classmates = ['aaa','bbb','ccc']
print(len(classmates))
print(classmates[-1])
print(classmates)
classmates.append('ddd')
print(classmates)
classmates.insert(0,'111')
print(classmates)
classmates.pop(1)
print(classmates)
print(classmates.pop())
print(classmates)
classmates[2]='333'
print(classmates)
list1=['aa','bb']
list2=['11','22',list1,'33']
print(list2)
print(list2[2][1])
print(len(list2))