class Solution:
    # time O(n)  space o(n)
    # 先计算s的counter, 然后一个个取出counter里的(需要while把freq有的一次全部去除 不能后append), 最后加上剩余counter里面的
    def customSortString(self, order: str, s: str) -> str:
        if not order or not s: return ""
        counter = collections.Counter(s)

        res = ""
        for char in order:
            if char in counter:    
                while counter[char] > 0: # 必须要把counter里的所有都取出append. eg. s='eqe' order='eq',output='eeq'
                    counter[char] -= 1
                    res += char
        for c, freq in counter.items():
            while counter[c] > 0: #此部分相同 也可以放入common method
                res += c
                counter[c] -= 1
        return res
