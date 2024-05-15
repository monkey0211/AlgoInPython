class Solution:
    # stack装ID: 还没有end的logId. 每碰到start就push+结算stack[-1]的结果, 碰到end就stack.pop()+计算结果. 
    # res array记录每个id的时长
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0]*n
        stack = []
        prevTime = 0
        for log in logs:
            logStr = log.split(":")
            id, string, currTime = int(logStr[0]), logStr[1], int(logStr[2])
            if string == "start": #calculate previous total, then push newId into stack
                if stack:
                    prevId = stack[-1]
                    res[prevId] += currTime - prevTime
                stack.append(id)
                prevTime = currTime
            else:
                currId = stack.pop()
                currTime += 1
                res[currId] += currTime - prevTime
                prevTime = currTime
        return res

