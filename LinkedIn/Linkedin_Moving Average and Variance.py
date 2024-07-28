# 转换为moving average问题: (n+1)的平均 用n的平均如何表示
# (n+1) = X_b(n) + (Xn+1 - X_b(n))/(n+1)

class Solution:
    def __init__(self):
        self.average = 0
        self.count = 0
        self.variance = 0 #moving variance
    
    def add(self, value):
        
        self.count += 1
        # 先求variance
        if self.count > 1:
            self.variance = (self.count - 2.0)/(self.count - 1.0)*self.variance + (value - self.average)*(value - self.average)/self.count
        # 再求average
        self.average += (value - self.average)/self.count
        return self.average, self.variance
    
# if use: E(x^2) - E(x)^2 will overflow.    
        

test = Solution()
print(test.add(10000000)) 
print(test.add(10000001))    
print(test.add(10000002))  
print(test.add(10000003))   
print(test.add(10000004))  
print(test.add(10000005))          