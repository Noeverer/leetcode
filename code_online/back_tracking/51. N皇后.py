#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 51. N皇后.py
@time: 2020-08-20 下午 2:15
"""
'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
 
提示：

皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，
就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自 百度百科 - 皇后 ）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def solveNQueens(self, N):
        checkerboard = ["." * N for i in range(N)]

        def check(row, col):
            for row_index in range(row):
                if row_index == row:
                    if "Q" in checkerboard[row_index]: return False
                if "Q" == checkerboard[row_index][col]: return False
            return check_left_up(row, col) and check_right_up(row, col)

        def check_left_up(row, col):
            while row > 0 and col > 0:
                row -= 1
                col -= 1
                if "Q" in checkerboard[row][col]: return False
            return True

        def check_right_up(row, col):
            while row > 0 and col < N - 1:
                row -= 1
                col += 1
                if "Q" in checkerboard[row][col]: return False
            return True

        def replace_char(string, char, index):
            string = list(string)
            string[index] = char
            return ''.join(string)

        def input(row):
            if row >= N: result.append(list(checkerboard))
            for input_col in range(N):
                if check(row, input_col):
                    checkerboard[row] = replace_char(checkerboard[row], "Q", input_col)
                    input(row + 1)
                    checkerboard[row] = replace_char(checkerboard[row], ".", input_col)

        result = []
        input(0)
        return result
