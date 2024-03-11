class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack or stack[-1]*a > 0 or stack[-1] < 0 and a > 0:
                stack.append(a)
            else:    
                flag = True #flag用来标记while结束之后 当前a是否需要入栈
                while stack and stack[-1]*a < 0:
                    if abs(a) > stack[-1]:
                        stack.pop()
                       
                    elif abs(a) == stack[-1]:
                        stack.pop()
                        flag = False
                        break #需要break: 此时a已经被碰撞掉 不需要继续while
                    else:
                        flag = False
                        break #需要break: 此时a已经被碰撞掉 不需要继续while
              
                if flag: 
                    stack.append(a)
         
        return stack