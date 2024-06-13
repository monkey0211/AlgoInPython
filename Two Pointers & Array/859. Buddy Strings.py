class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # 如果s == goal, 1)如果有任何一个char重复两次以上 就一定可以switch -> True
        counter = collections.defaultdict(int)
        if s == goal:
            for char in s:
                counter[char] += 1
                if counter[char] > 1:
                    return True
        # general情况: 逐个比较两个string 如果有不同就记录index, 最后return两个s[indexList[0]] == goal[indexList[1]] 是否相等
        indexList = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                indexList.append(i)
                if len(indexList) > 2:
                    return False
        return len(indexList) == 2 and s[indexList[0]] == goal[indexList[1]] and goal[indexList[0]] == s[indexList[1]]
        