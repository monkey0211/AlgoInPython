class Solution:
    # 每走一步都需要有权重, 所以要用heap, 不是queue: 每一步都贪心的走当前cost最小的
    # 对每一个direction: while 一直走, step+1, 直到撞墙, 然后把cost = step+当前积累的distance放入heap
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        visited = set()
        pq = [(0, start[0], start[1])]

        while pq:
            dist, x, y = heapq.heappop(pq) # [cost, (i, j)]
            if x == destination[0] and y == destination[1]:
                return dist

            if (x,y) in visited:
                continue
            visited.add((x,y))

            # for each of the four directions we can go
            for dx, dy in[[0,1],[0,-1],[1,0],[-1,0]]:
                newx = x + dx
                newy = y + dy
                steps = 0 # 撞墙之前能走多少步

                while 0 <= newx < len(maze) and 0 <= newy < len(maze[0]) and maze[newx][newy] == 0:
                    #一直向一个方向走
                    steps += 1
                    newx += dx
                    newy += dy
                if steps > 0:
                    heapq.heappush(pq, (steps + dist, newx - dx, newy - dy)) #退回一步 因为while里面已经走出去了(越界)

        return -1

        