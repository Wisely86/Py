#!/usr/bin/env python3
# -*- coding: utf-8 -*-
names = ['Michael', 'Bob', 'Tracy']
for n in names:
    print(n)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
for i in range(101):
    sum = sum + i
    if i == 56:
        print(i)
        break
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']

for i in L:
    if 'Lisa' == i:
        break
    print(i);

for i in L:
    if 'Lisa' == i:
        continue
    print(i);

print("#####111111111#################")
x = 0
L = ['Bart', 'Lisa', 'Adam']
while x < len(L):
    if 'Lisa' == L[x]:
        continue
    x = x + 1
    print(L[x])
print("###################################")

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)