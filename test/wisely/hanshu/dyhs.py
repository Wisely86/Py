#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def my_max(s):
    if s >= 10:
        return s
    else:
        return 9


#print(my_max(2))


def nullpass():
    pass


def powerx(x,y = 3):
    t = 1
    while(y > 0):
        y = y - 1
        t = x * t
    return t

def listtst(list = None):
    if list is None:
        list = []
    list.append('END')
    return list

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f2(1, 2 ,d=1)


def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')


def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)
