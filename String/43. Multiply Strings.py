class Solution:
    # 两位数相乘, 最多长度是len(nums1)+len(nums2). 每个位数相乘都最多2位,  low在[i+j+1] high在[i+j]
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        res = [0]*(len(num1) + len(num2))

        #倒着计算
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                digit = int(num1[i]) * int(num2[j])
                sum = res[i+j+1] + digit #低位的值
                res[i+j+1] = sum % 10
                carry = sum // 10 
                res[i+j] += carry #更新高位

        #变成string之后再去掉开头是0的
        res = "".join(map(str, res))
       
        return res.lstrip("0")