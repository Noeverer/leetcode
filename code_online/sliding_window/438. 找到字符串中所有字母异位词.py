#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Robot Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 438. 找到字符串中所有字母异位词.py
@time: 2020-08-20 下午 1:35
"""
'''
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = collections.defaultdict(int)
        valid,L,R,ans = 0,0,0,[]
        while R<len(s):
            # 判断右边界
            c = s[R]
            R += 1
            window[c] += 1
            if need[c]==window[c]:
                valid += 1
            while valid == len(need):
                c = s[L]
                L += 1
                if need[c] == window[c] :
                    valid -= 1
                    if sum(need.values()) == sum(window.values()):
                        ans.append(R - len(p))
                window[c]-=1
        return ans