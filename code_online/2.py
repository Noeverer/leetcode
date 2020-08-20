#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Robot Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 2.py
@time: 2020-08-13 下午 10:55
"""
import sys

# line = list(map(int, sys.stdin.readline().split()))
#
# n, m = line[0], line[1]
#
# cache = []
#
# for _ in range(n):
#     tmp = list(map(int, sys.stdin.readline().split()))
#     cache.append(tmp)
#
# print(cache)

# cache = {0:[2, 4], 1:[2, 35], 2:[1, 43], 3:[2, 10]}
#
# tmp = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     tmp[i][i] = cache[i]
# output = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         if tmp[i][j-1][0] + cache[j][0] <= m:
#             tmp[i][j] = [tmp[i][j-1][0] + cache[j][0], tmp[i][j-1][1] + cache[j][1]]
#             print(tmp[i][j])
#             output = max(output, tmp[i][j][1])
#         else:
#             break

for 选择 in [选择列表]:



n, m = 4, 6
cache = [[2, 4], [2, 35], [3, 43], [2, 10]]
output = []
def helper(start, curr):
    if len(curr) ==k:
        output.append(curr[:])
        # return
    for i in range(start,n):
        if cache[i] in curr:
            continue
        curr.append(cache[i])
        helper(i+1,curr)
        curr.pop()
for k in range(n+1):
    helper(0, [])
max_val = 0
for item in output:
    time = 0
    value = 0
    for i in item:
        time += i[0]
        value += i[1]
    if time <= m:
        max_val = max(max_val, value)
print(max_val)

if __name__=="__main__":
    # print("******8")
    # print(tmp)
    print(output)
    print(len(output))
    print(max_val)
    for item in output:
        print(item, sum([i[0] for i in item]), sum([i[1] for i in item]))