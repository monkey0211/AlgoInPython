class Solution:
# DP 贪心: 先找出次数最多的task作为benchmark. 
# 前面n-1组都需要加idle: (maxFreq-1)*(n+1)
# 最后还剩一组k个 不需要加idle: 也就是最大频率的task的个数. 次数最多的元素有多少个 补充在最后
# 特殊情况n=0(或者n不够长 最短的情况就是len(tasks) 最后return length和上面的Max. 需要记住 难证明
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks: return 0
        counter = collections.Counter(tasks)

        # cnt: the number of tasks that has the max count. 
        # maxValue: value of max count
        cnt, maxValue = 0, max(counter.values())
        for k, v in counter.items():
            if v == maxValue:
                cnt += 1
        intervals = (maxValue - 1)*(n+1) + cnt
        return max(len(tasks), intervals)
