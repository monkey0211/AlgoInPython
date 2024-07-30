#如何从 N(>>M)的样本中选出M个sample并分层抽样 -> reservoir sampling
# input: billions of training examples in a file, each has one of 4 class labels. 
# output: select M random samples from each class c={1,2,3,4}

# 一共有N个sample 如何选M个(假设一个category):
# maintain an array of fixed size M. For each coming example j, if array not full, append. 
# else, 随机产生[0,j]随机数, 如果j <= M, replace j with nums[j].
# 这样可以保证每一个被抽取的概率是M/N
import collections
import random


class Example:
    def __init(self, label):
        self.label = label
    def getLabel(self):
        return self.label
        
class Solution:
    def stratifiedSample(sampleIterator: str, requiredCountMap):
        counter = collections.defaultdict(int) # label -> cumulative cnt
        reservoir = collections.defaultdict(list) # label->list of samples
        
        
        while sampleIterator.hasNext(): # or for each samples
            sample = sampleIterator.next() # or samples[i]
            label = sample.getLabel()
            currRes = reservoir[label] # get现在的reservoir
            cnt = counter[label] # get现在的cnt
            M = requiredCountMap[label] #required count
            
            if len(currRes) < M:
                reservoir[label].append(sample)
            else:
                index = random.randint(0, cnt) #这里取下标j, 包括自己 一共cnt+1个
                if index < M: # 不取等
                    reservoir[label][index] = sample
            counter[label] += 1
        return reservoir
            
# 直接想法: 给N个数 每一个都random assgin一个number, 然后sort取前M个 O(nlogN)不好, 存不下.
# how to test:1)固定参数test 2) run 10000次, 每个被选中的item被选中次数m p = m/10000, 和M/N比较
        