#!/usr/bin/python3.6
#coding:utf-8

import sys
import os
import re

'''
2020.08.15携程
铺砖
现在有充足的长度为a和长度为b的两种规格瓷砖。现在从这些瓷砖中任取k块来铺路，按递增的顺序输出所有可能的铺成道路的长度。
例子
输入a、b、k
1
2
3
输出一个数组
[3,4,5,6]
'''

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
#******************************开始写代码******************************
while 1:
    def divingBoard(a, b, k):
        choose = [a,b]
        output = set()
        def back(curr):
            if len(curr)==k:
                output.add(sum(curr[:]))
                return
            for i in choose:
                curr.append(i)
                back(curr)
                curr.pop()
        back([])
        return list(output)
    _a = 1
    _b = 2
    _k = 3
    res = divingBoard(_a, _b, _k)
    print(sorted(res))
    break