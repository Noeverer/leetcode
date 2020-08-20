#!/usr/bin/python3.6
#coding:utf-8
'''
美团8.15开发：求一个数连续的质数和等于这个数
ex1：n=41，连续质数=[1, 2, 3, 5, 7, 11],其中sum([5,7])=12,符合条件
'''
import math
def isp(n):
    p=[1,]
    for i in range(2,n+1):
        m = 0
        for j in range(1,i+1):
            if i%j==0:
                m+=1
        if m==2:
            p.append(i)
    return p
while 1:
    n= int(12)
    all_num = isp(n)
    print(all_num)
    ans = 0
    for i in range(1,len(all_num)):
        j = 0
        while i+j<=len(all_num):
            if sum(all_num[j:i+j]) == n:
                ans += 1
                print(all_num[j:i+j])
            j+=1
    print(ans)
    break