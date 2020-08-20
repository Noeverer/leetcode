#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Robot Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 567. 字符串的排列.py
@time: 2020-08-20 下午 1:20
"""
'''
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
 

示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import collections
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = collections.defaultdict(int)
        valid, L, R, ans = 0, 0, 0, False
        while R < len(s2):
            # 扩大右边界
            c = s2[R]
            R += 1
            window[c] += 1
            # valid设置有效个数
            if need[c] == window[c]:
                valid += 1
            while valid == len(need):
                # 收缩左边界
                # ans = True
                if len(s1) == R - L:
                    ans = True
                c = s2[L]
                L += 1
                if need[c] == window[c]:
                    valid -= 1
                window[c] -= 1  # 注意删除左边个数统计
        return ans