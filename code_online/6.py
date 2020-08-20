#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Robot Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 6.py
@time: 2020-08-19 下午 7:11
"""
M,N = 10,20
output = [17,37,57,77,97]
for i in range((M*N)//100):
    if i != 0:
        out = [i*100+j for j in output]
        output.extend(out)
print(output)  # 生产出所有符合的坐标

count = 0
for idx,find in enumerate(output):  # 查找计数的点
    que = min(M,N) //2
    for i in range(que):
        up_row = N-i*2
        df = find - count
        count += up_row
        while count >= find:
            output[idx] = [i,df+i]

        right_col = M-2-i*2
        df = find-count
        count += right_col
        while count >= find:
            output[idx]=[df+i,i]

        low_row = N-i*2
        df = find - low_row
        count += low_row
        while count >= find:
            output[idx]=[M-i,N-i-df]

        left_col = M-2-i*2
        df = find - left_col
        count += left_col
        while count >= find:
            output[idx]=[M-i-df,N-i]










