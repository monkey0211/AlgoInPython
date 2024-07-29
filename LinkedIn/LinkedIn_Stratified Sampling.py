#如何从 N(>>M)的样本中选出M个sample并分层抽样 -> reservoir sampling
# input: billions of training examples in a file, each has one of 4 class labels. 
# output: select M random samples from each class c={1,2,3,4}

# 一共有N个sample 如何选M个(假设一个category):
# maintain an array of fixed size M. For each coming example j, if array not full, append. 
# else, 随机产生[0,j]随机数, 如果j <= M, replace j with nums[j].
# 这样可以保证每一个被抽取的概率是M/N
import collections


class Example:
    def __init(self, label):
        self.label = label
    def getLabel(self):
        return self.label
        
class Solution:
    def stratifiedSample(sampleIterator: str, requiredCountMap):
        counter = collections.defaultdict(int) # label -> cumulative cnt
        reservoir = collections.defaultdict(list) # label->list of samples
        
        # for label in labelToCount:
        #     reservoir[label].append(sample)
        #     counter[label] += 1
        
        while sampleIterator.hasNext(): # or for each samples
            sample = sampleIterator.next() # or samples[i]
            label = sample.getLabel()
            currRes = reservoir[label] # get现在的reservoir
            cnt = counter[label] # get现在的cnt
            M = requiredCountMap[label] #required count
            
            if len(currRes) < M:
                reservoir[label].append(sample)
            else:
                random = random.randomint(0, cnt + 1) #??
                if random < M: # 不曲等?
                    reservoir[label] = sample
            counter[label] += 1
                
            
# 直接想法: 给N个数 每一个都random assgin一个number, 然后sort取前M个 O(nlogN)不好, 存不下.
# TODO: how to test:    
        