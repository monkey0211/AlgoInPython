class Solution:
    # two pointer: 先对调firstList&secondList if firstList大
    # from left to right, iterate each pair find maxStart and minEnd. if <, append to res.
    # smaller endpoint, move to next pointer
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        if not firstList or not secondList: return res

        i, j = 0, 0
        if firstList[0][0] > secondList[0][0]:
                firstList, secondList = secondList, firstList
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]
            maxStart = max(first[0], second[0])
            minEnd = min(first[1], second[1])
            
            if maxStart <= minEnd:
                res.append((maxStart, minEnd))
            if first[1] == minEnd:
                i += 1
            else:
                j += 1
        return res
        