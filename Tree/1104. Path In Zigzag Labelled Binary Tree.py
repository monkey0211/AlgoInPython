'''
思路:找规律
对于label为x的点 如果不考虑题设中的“奇数列翻转” 那么它的parent node编号是(x//2)
几个性质: (画图) 把每层的数字用二进制表示 如果该层被翻转 对应的数 会变成除了最高位外 剩余位与1111进行异或的结果

分情况讨论:
1.如果label所在的层未被翻转 只需要翻转1,3,5,7...层
2.如果label所在层翻转: 可以想象成 把整棵树都翻转 然后再翻转1,3,5,7...层 转化为情况1
这里等价为 翻转了0,2,4,6...层 因为某层如果翻转了两次 等于没有翻转

这棵树是完全二叉树 则可以有:若root编号为1 则任意一个节点x左儿子编号为2x 右儿子编号为2x+1
对于任意一个节点x 父节点编号是x//2 (向下取整) 但是该题是奇数层从左到右编号，偶数层从右到左编号。

首先能确定的是每层的编号还是那些 只不过次序变换了 
若当前节点编号是x 父节点编号本应是x//2 本应父节点是上一层从左到右第k个节点 则变成从右到左第k个节点。

1. 计算n在第几层
2. 从n开始往上枚举变换后的父节点编号
时间复杂度O(logN)
'''
from typing import List

class Solution:
    def get_start(self, lvl:int) -> int:
        return pow(2, lvl - 1)

    def get_end(self, lvl:int) -> int:
        return self.get_start(lvl + 1) - 1

    def pathInZigZagTree(self, label: int) -> List[int]:
        if not label:
            return []
        lvl = 1
        while self.get_end(lvl) < label:
            lvl += 1
        ret = [0] * lvl
        cur_lvl, cur_label = lvl, label
        # label和level都从1开始算
        while cur_label > 0 and cur_lvl > 0:
            ret[cur_lvl - 1] = cur_label
            parent = cur_label // 2
            start = self.get_start(cur_lvl - 1)
            end = self.get_end(cur_lvl - 1)
            parent = end - (parent - start)
            cur_label = parent
            cur_lvl -= 1
        return ret
        