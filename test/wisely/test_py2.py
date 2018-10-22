#!/usr/bin/env python 
# -*- coding:utf-8 -*-
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')

print(len('abcdef'))
print(len('汉字'.encode('utf-8')))
print('中文')
#占位符%d，%s，%x，%f
print('您好，您本月消费%d元，请在%s前进行缴费' %(120,'10月31日前'))