#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Robot Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 3. 无重复字符的最长子串.py
@time: 2020-08-20 下午 1:38
"""
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:return 1
        window = collections.defaultdict(int)
        L,R,ans = 0,0,0
        while R<len(s):
            # 判断右边界
            c = s[R]
            R += 1
            window[c] += 1
            # print(window,1212)
            while window.get(s[R-1]) and window.get(s[R-1])>1:
                # 判断左边界
                c = s[L]
                L += 1
                window[c] -= 1
            ans = max(ans,R-L) # 最后确认window里面符合条件，更新ans
        return ans if ans > 0 else 0