class Solution:
    #results list里面一共五个candidate: 
    # 1) 1001 2) 99
    # 3) mid digit+1的翻转 eg. 123->131
    # 4) mid digit-1的翻转 eg. 123->111
    # 5) mid digit的翻转 eg. 123->121
    def nearestPalindromic(self, n: str) -> str:
        results  = []
        length = len(n)

        if length == 1:
            return str(int(n) - 1)

        results.append(10 ** length + 1) # n的位数的下一位,"1001"
        results.append(10 ** (length - 1) - 1) # n的位数的少一位, "99"

        mid = (length + 1) //2
        prefix = int(n[:mid])
        prefixes = [prefix , prefix - 1, prefix + 1]
 
        for i in prefixes:
            leftHalf = str(i)    
            if length % 2 == 1: #如果总长度为奇数, 去掉中间的数, 再和reverse prefix拼接
                leftHalf = leftHalf[:-1]
            candidate = str(i) + leftHalf[::-1]
            results.append(int(candidate))

        minDiff = float('inf')
        result = tip = int(n)

        #比较5个candidate 选diff最小的那个
        for i in range(5):
            if results[i] != tip and minDiff > abs(results[i] - tip):
                print(results[i], tip)
                minDiff = abs(results[i] - tip)
                result = results[i]
            elif abs(results[i] - tip) == minDiff: #如果两个candidate diff相同, 选小的那个
                result = min(result, results[i])

        return str(result)