class Solution:
#two pointer: 每次拿cnt小的 减去, 然后cnt小的指针向前移动.
#处理res: 如果res[-1]已经有了这个乘积,改变res[-1][1]累加currMin, 没有就append一个新的tuple
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        if not encoded1 or not encoded2:
            return []
        i, j = 0, 0
        res = []
        
        while i < len(encoded1) and j < len(encoded2):
            curValue = encoded1[i][0] * encoded2[j][0]
            cnt1 = encoded1[i][1]
            cnt2 = encoded2[j][1]
            
            if cnt1 < cnt2:
                i += 1
                curFreq = cnt1
                encoded2[j][1] = cnt2 - cnt1 #这里需要改写encoded的值 为下一次循环做准备. 否则下一次再拿cnt2会把这次的值覆盖
            elif cnt1 > cnt2:
                j+= 1
                curFreq = cnt2
                encoded1[i][1] = cnt1 - cnt2
            else:
                i += 1
                j += 1
                curFreq = cnt1
            
            #处理res: 如果res[-1]已经有了这个乘积,改变res[-1][1]累加currMin, 没有就append一个新的tuple
            if res and res[-1][0] == curValue:
                res[-1][1] += curFreq
            else:
                res.append([curValue, curFreq])
        return res