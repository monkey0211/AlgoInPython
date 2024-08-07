# (队列实现滑动窗口) O(n)
# 首先我们可以知道，对于每个位置而言，只有初始状态和总共被反转了多少次决定了自己最终的状态。另一方面，我们知道每一个长度为K的区间，最多只会被反转一次，因为两次反转后对最终结果没有影响。
# 基于此，我们从前往后遍历数组，如果遇到一个0，我们将当前位置开始的长度为k区间的区间反转。如果遇到0时，剩下的区间长度不足K说明我们没有办法完成反转。但是如果我们每次反转当前区间时，将区间内每个数都取反，时间复杂度是O(n∗k)的，这样是不够快的。需要优化一下，我们再考虑每个位置上的元素，他只会被前面K - 1个元素是否被反转所影响，所以我们只需要知道前面k - 1个元素总共反转了多少次(更进一步的说我们只关系反转次数的奇偶性)。
# 我们使用一个队列保存i前面k - 1个位置有多少元素被反转了。
# 如果队列长度为奇数，那么当前位置的1被变成0了需要反转，如果为偶数，说明当前位置的0还是0，需要反转。
# 如果最后k - 1个位置还有0的话说明失败。否则将i加入队列，更新答案。
# 时间复杂度：每个元素最多被进入队列和出队列一次，所以总的时间复杂度为O(n)

# BFS: queue.
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n, ret = len(nums), 0
        queue = deque([]) # 存储当前位置的 前k - 1个元素中 需要翻转的元素下标 也代表了能影响到当前位置的翻转次数
        for i in range(n):  # 从前往后遍历每个元素
            while queue and queue[0] + k <= i:  # 队列元素中的个数大于等于k 需要pop最早入队的 它影响不到当前i位置
                queue.popleft()
            
            if nums[i] == len(queue) % 2: # 两种情况当前位置需要翻转 1.队列长度是奇数且当前值是1(奇数长度的队列会把当前值转成0) 2.队列长度是偶数且当前值是0(之后需要转成1)
                if i + k > n:   # 最后元素不足k个了 无论如何也无法满足条件: 一次翻转必须转exact k个 无解  
                    return -1
                queue.append(i) # 当前下标入队
                ret += 1        #更新所求答案
        return ret