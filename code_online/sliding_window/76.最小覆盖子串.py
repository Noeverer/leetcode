#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Robot Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 76.最小覆盖子串.py
@time: 2020-08-20 上午 11:20
"""
'''
给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入：S = "ADOBECODEBANC", T = "ABC"
输出："BANC"


提示：


	如果 S 中不存这样的子串，则返回空字符串 ""。
	如果 S 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = collections.defaultdict(int)
        valid,L,R,ans = 0,0,0,(-1,len(s))
        while R<len(s):
            # 扩大右边界
            c = s[R]
            R += 1
            window[c] += 1
            # valid设置有效个数
            if need[c]==window[c]:
                valid += 1
            while valid == len(need):
                # 收缩左边界
                ans = (L,R) if R-L < ans[1]-ans[0] else ans
                c = s[L]
                L += 1
                if need[c] == window[c]:
                    valid -= 1
                window[c]-=1 # 注意删除左边个数统计
        return s[ans[0]:ans[1]] if ans[0] != -1 else ''

sol = Solution()
res = sol.minWindow("ADOBECODEBANC","ABC")
print(res)
