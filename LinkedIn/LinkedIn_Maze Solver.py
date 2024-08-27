# You are given a NxN matrix of chars representing a maze. Char 'B' means wall and char "#' means road. Here is an example:
# [["#',"#','B','B'],
# ["#',"#',"#',"#'],
# [“B”,“B”,“#”,“#”],
# ["#',"#',"#',"#']]
# Suppose there is a robot standing on (0,0). He is supposed to be moving around only in four directions: Up, DOWN, LEFT, RIGHT. Also he cannot step on to walls. Write a function which will calculate if it is possible for him to go from (0,0) to (n-1,n-1)
# Function: 
# hasWay(matrix, n)
from collections import deque

# BFS: time o(n^2) space o(n^2)
def hasWay(matrix, n):
    # 检查矩阵是否为空或者起点或终点是墙
    if not matrix or matrix[0][0] == 'B' or matrix[n-1][n-1] == 'B':
        return False

    # 定义四个移动方向：右、下、左、上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 初始化队列并将起点 (0, 0) 加入队列
    queue = deque([(0, 0)])
    
    # 标记已经访问过的位置，防止重复访问
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True

    # 开始BFS搜索
    while queue:
        x, y = queue.popleft()

        # 如果到达终点，返回True
        if x == n-1 and y == n-1:
            return True

        # 遍历四个方向
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # 检查新的位置是否在边界内，且未访问过，并且不是墙
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y] and matrix[new_x][new_y] == '#':
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))

    # 如果BFS结束还没有到达终点，返回False
    return False

# method2: DFS: time o(n^2) space o(n^2)
def hasWay(matrix, n):
    # 检查矩阵是否为空或者起点或终点是墙
    if not matrix or matrix[0][0] == 'B' or matrix[n-1][n-1] == 'B':
        return False

    # 定义四个移动方向：右、下、左、上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 访问标记矩阵，防止重复访问
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    # 定义DFS函数
    def dfs(x, y):
        # 如果到达终点，返回True
        if x == n-1 and y == n-1:
            return True

        # 遍历四个方向
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # 检查新的位置是否在边界内，且未访问过，并且不是墙
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y] and matrix[new_x][new_y] == '#':
                visited[new_x][new_y] = True  # 标记为已访问
                if dfs(new_x, new_y):  # 递归探索
                    return True
                visited[new_x][new_y] = False  # 如果没找到路径，回溯

        # 如果所有方向都无法通行，返回False
        return False

    # 从起点开始DFS
    visited[0][0] = True
    return dfs(0, 0)
