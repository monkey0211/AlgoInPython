# intput: a method getRandom01Biased() that generates a random integer in [0, 1] 
# where 0 is generated with prob p and 1 is with (1-p)
# output: a method getRandom06Uniform() that generates a random integer in [0, 6] with uniform prob

import math
import random
class Solution: 
    def getRandom01Biased(self):
        return 1 if math.random() >= 0.7 else 0

    # 抛两次 01 or 10 -> p(1-p)相等, 11->p^2, 00->(1-p)^2
    def getRandom01Uniform(self):
        num1 = self.getRandom01Biased()
        num2 = self.getRandom01Biased()
        num = 10*num1 + num2
        # num could be: 11,10,01,0
        if num == 10:
            return 0
        elif num == 1:
            return 1
        else:
            return self.getRandom01Uniform() #继续抛
    
    #用三位数表示 000-111 一共8个candidate 二进制表示[0,6],if 7,重新抛三次. 
    def getRandom06Uniform(self):
        res = self.getRandom01Uniform() + 2 * self.getRandom01Uniform() + 4 * getRandom01Uniform()
        if res < 6:
            return res 
        else:
            return self.getRandom06Uniform() #重新来

# follow up: 
# 1. how to test? how to test uniform distribution
    # run for 10000 times. compare p and sum(res)/cnt(res)
# 2. how to generate random integer in any range[x, y]
    # x + int(getRandom01Uniform() * (y - x + 1)) 
# 3. given getRandom01Uniform() how to implement getRandom01Biased with outcome p and (1-p)
    # Generate a sequence of bits using getRandom01Uniform().
    # Interpret this sequence as a binary fraction to approximate a uniform random number between 0 and 1.
    # Compare this number to p return 1 else return 0

    # def getRandom01Biased(p):
    #     if getRandom01Uniform() < p:
    #         return 1
    #     else:
    #         return 0


# Variance: given random7 return random10
# Testing the rand10 function:
# 1. 先扔两次 产生49个数: num = ((first - 1) * 7 + second)
# 2. 如果num<40, return num%10 + 1 如果大于,重复random10.

import random

def rand7():
    return random.randint(1, 7)

def rand10():
    while True:
        num1 = rand7()
        num2 = rand7()
        result = (num1 - 1) * 7 + num2  # Generates a number between 1 and 49
        if result <= 40:
            return (result % 10) + 1


for _ in range(10):
    print(rand10())
