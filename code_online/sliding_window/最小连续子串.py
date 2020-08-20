#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Robot Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 最小连续子串.py
@time: 2020-08-17 下午 8:46
"""
import collections
from collections import Counter

def minWindow1(s: str, t: str):
    need = {}
    window = {}
    for tt in t:
        if not need.get(tt):
            need[tt] = 0
        need[tt] += 1
    print(need)
    left,right = 0,0
    valid = 0
    start,win_len =0, float('inf')
    while right<len(s):
        can_char = s[right]
        right += 1
        if need.get(can_char):
            if not window.get(can_char):
                window[can_char] = 0
            window[can_char] += 1
            if window[can_char] == need[can_char]:
                valid += 1
        while valid == len(need):
            if right-left < win_len:
                start = left
                win_len = right - left
            un_char = s[left]
            left += 1
            if need.get(un_char):
                if window[un_char] == need[un_char]:
                    valid -= 1
                    window[un_char] -= 1
    print(start,win_len)
    return s[start:win_len] if win_len != float('inf') else ''

def minWindow(s: str, t: str) -> str:
    '''
    76.最小覆盖子串
    输入：S = "ADOBECODEBANC", T = "ABC"
    输出："BANC"
    '''
    need = Counter(t)
    window = dict.fromkeys(need.keys(), 0)
    valid, L, R, ans = 0, 0, 0, (-1, len(s))
    while R < len(s):
        c = s[R]
        R += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        while valid == len(need):
            ans = (L, R) if R - L < ans[1] - ans[0] else ans
            c = s[L]
            L += 1
            if c in need:
                if window[c] == need[c]:
                    valid -= 1
                window[c] -= 1
    if ans[0] == -1:
        return ""
    return s[ans[0]:] if ans[1] == len(s) else s[ans[0]:ans[1]]


def minwin(s):
    '''
    最小连续不重复子串
    :param s:
    :return:
    '''
    window = collections.defaultdict(int)
    valid,L,R,ans = 0,0,0,0
    while R<len(s):
        # 判断右边界
        c = s[R]
        R += 1
        window[c] += 1
        while window.get(s[R-1]) and window.get(s[R-1])>1:
            ans = max(ans,R-L)
            c = s[L]
            L += 1
            window[c] -= 1
    return ans-1

res = minwin("abcabcdbb")
print(res,232323)