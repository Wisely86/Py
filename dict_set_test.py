#!/usr/bin/env python3
# -*- coding: utf-8 -*-
dict1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dict1.keys())
print(dict1.values())
print(dict1.get('Wisely'))
print(dict1.get('Wisely','主键不存在'))
dict1['Bob'] = 90
print(dict1)
print('Wisely' in dict1)
dict1.__setitem__('wisely',99)
print(dict1)
print(dict1.pop('Bob'))
print(dict1)
print("##########SET#################")
set1 = set([1, 2, 3])
print(set1)
set1 = set([1, 1, 2, 2, 3, 3])
print(set1)
set1.add('5')
set1.add('6')
set1.add('1')
print(set1)
set1.add('1')
print(set1)
set1.remove(1)
print(set1)

s1 = set([1, 2, 3])
s2 = set([1, 3, 4])

s = s1 & s2
print(s)
s = s1 | s2
print(s)

list1 = [3,2,1]
print(list1)
list1.sort()
print(list1)
setList = set(list1)
print(setList)