# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0

        # 先找一个不认识0的人 作为candidate
        for i in range(1, n):
            if not knows(i, candidate):
                candidate = i
        # 如果1)candidate==j 2) j认识candidate but candidate不认识j ->continue
        for j in range(n):
            if j == candidate or knows(j, candidate) and not knows(candidate, j):
                continue
            #如果找了所有人都valid
            return -1
        return candidate
        