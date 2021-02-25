'''
Description: Fibonacci
version: 
Author: Jutraman
Email: jutraman@aliyun.com
Date: 2021-02-24 23:35:35
LastEditors: Jutraman
LastEditTime: 2021-02-24 23:59:13
Github: https://github.com/Jutraman
'''

#! /usr/bin/python

def fibonacci(n):
    if n==0: return 0
    if n==1: return 1
    return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(4))