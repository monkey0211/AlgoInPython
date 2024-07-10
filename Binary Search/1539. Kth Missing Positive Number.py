class Solution:
   
    # 归纳:(val(i) - i - 1)可以得出 在idx i之前 一共丢失了几个数字
    # 假如通过二分 找到了某个idx==m 使得:val(m)-m-1==k 根据上述观察 在idx==m之前丢了k个数字
    # 下一步需要知道这第k个丢失数是什么
    # 如果不丢数: val(i)==i+1 
    # 数与数之间 如果每丢一个数 下一个数字数值就比丢失的这个数大1 举例: 
    # idx: 0	 1	 2	 3
    # val: 1	 3	 6	 8
    # val1和3之间丢了2 如果k==1 二分最终停在idx==1 缺的数字就是二分停止的idx+1==2

    # 所以如果在idx==m上 已知丢了k个数 那么第k个丢掉的==m + k

    # 注意上面所有的论述是假设 二分停止的idx之前一定是有缺数字的 即:要找的miss num < 当前的val(idx)
    # 还有一类情况是 没有缺数字 或者说 要找的数字是在idx的右边 此时二分停止的位置指向数组最大值(也就是最靠近missing num的位置)
    # 这时miss num == idx+1+k, 其中idx+1是当前位置不缺数的情况下理论上的数值 需要再往右数k个得到missing num 
    
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if (arr[mid] - mid - 1) < k:
                left = mid
            else:
                right = mid
        # diff是判断二分停止的位置right 左边缺不缺数字.
        # 有可能缺的数字在右边 此时right指向数组最后一个元素(二分认为离要找的元素最近的元素了)
        # diff = arr[right] - (right + 1) - k

        # if diff >= 0: # 左边缺数字
        #     return right + k
        # else:         # 要找的数在右边
        #     return right + 1 + k

        if arr[left] - (left + 1) >= k:
            return left + k
        elif arr[right] - (right + 1) >= k:
            return right + k
        else:
            return right + k + 1