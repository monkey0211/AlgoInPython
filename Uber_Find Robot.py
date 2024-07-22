import collections
from math import sqrt
import math
# https://leetcode.com/discuss/interview-experience/4718477/Uber-or-Phone-Screen-or-Amsterdam/
# Given two inputs,

# First input is the location map, a 2D array
# | O | E | E | E | X |
# | E | O | X | X | X |
# | E | E | E | E | E |
# | X | E | O | E | E |
# | X | E | X | E | X |

# O = Robot, E = Empty, X = blocker

# Second input is the query. It’s a 1D array consisting of distance to the closest blocker in the order from left, top, bottom and right
# [2, 2, 4, 1] -> This means distance of 2 to the left blocker, 2 to the top blocker, 4 to the bottom blocker and 1 to the right blocker

# The location map boundary is also considered blocker, meaning if the robot hits the boundary it also means it’s hitting the blocker.

# Task: Write a function that takes these two inputs and returns the index of the robots (if any) that matches the query that we’re looking for.
# Answer: [[1, 1]]

# 解法 time o(mn)
# 对每个robot, 1st traversal 先计算 left and top distances. 如果是Blocker就更新left and top boundary.
# 2nd traversal 再计算 bottom and right distances.
# 3rd traversal: find the robot matching query
from collections import defaultdict
from typing import List

LEFT = 0
TOP = 1
BOTTOM = 2
RIGHT = 3
def findRobot(matrix, query) -> List[int]:
  
    map = defaultdict(lambda: [None] * 4)
    top = [-1] * len(matrix[0])
    for i in range(len(matrix)):
        left = -1 #左边界是-1
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'O':
                map[(i, j)][LEFT] = abs(j - left)
                map[(i, j)][TOP] = abs(i - top[j])

            if matrix[i][j] == 'X': #如果是blocker更新左边界和top边界
                left = j
                top[j] = i

    bottom = [len(matrix)] * len(matrix[0])
    
    for i in range(len(matrix)-1, -1, -1):
        right = len(matrix[0])
        for j in range(len(matrix[0])- 1, -1, -1):
            if matrix[i][j] == 'O':
                map[(i, j)][BOTTOM] = abs(i - bottom[j])
                map[(i, j)][RIGHT] = abs(j - right)

                # if map[(i, j)]== query:
                #     return [i, j]

            if matrix[i][j] == 'X':
                right = j
                bottom[j] = i
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if map[(i, j)]== query:
                return [i, j]

    return [-1, -1]
        

matrix = [
  ['O','E','E','E','X'],
  ['E','O','X','X','X'],
  ['E','E','E','E','E'],
  ['X','E','O','E','E'],
  ['X','E','X','E','X']
]

query = [2, 2, 4, 1] 
print(findRobot(matrix, query))