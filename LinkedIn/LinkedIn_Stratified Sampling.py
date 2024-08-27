#如何从 N(>>M)的样本中选出M个sample并分层抽样 -> reservoir sampling
# input: billions of training examples in a file, each has one of 4 class labels. 
# output: select M random samples from each class c={1,2,3,4}

# 一共有N个sample 如何选M个(假设一个category):
# maintain an array of fixed size M. For each coming example j, if array not full, append. 
# else, 随机产生[0,j]随机数, 如果j <= M, replace j with nums[j].
# 这样可以保证每一个被抽取的概率是M/N
import collections
import random
import threading

class SampleIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.lock = threading.Lock()  # InstanceIterator 
        
    def has_next(self) -> bool:
        with self.lock:
            return self.cur < self.end
    
    def next(self) -> Instance:
        with self.lock:
            if self.cur >= self.end:
                raise StopIteration
            instance = Instance(f"Label_{self.cur}")  # 创建新的 Instance 对象
            self.cur += 1
            return instance
    
class Sample:
    def __init__(self, label):
        self.label = label
        # Instance 类不需要任何同步机制
        # 1. 它是不可变的（label 在初始化后不会改变）
        # 2. 每次调用 InstanceIterator.next() 都会创建一个新实例
        # 3. 它没有修改内部状态的方法
    
    def getLabel(self):
        return self.label
        
class Solution:
    def stratifiedSample(sampleIterator: SampleIterator, requiredCountMap):
        counter = collections.defaultdict(int) # label -> cumulative cnt
        reservoir = collections.defaultdict(list) # label->list of samples
        
        lock = threading.Lock() #followup加锁: 这个锁用于保护reservoir和counter
        
        while sampleIterator.hasNext(): # or for each samples
            sample = sampleIterator.next() # or samples[i]
            label = sample.getLabel() 
            
            with lock: #followup加锁:
                
                currRes = reservoir[label] # get现在的reservoir
                cnt = counter[label] # get现在该label一共数过的cnt
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
# followup: implement a parallelism version TODO
s1 = Sample("blue")
s2 = Sample("blue")
s3 = Sample("yellow")
s4 = Sample("yellow")
s5 = Sample("yellow")
samples = [s1, s2, s3, s4, s5]
requiredCountMap = {"blue": 1, "yellow":2}
test = Solution()
print(test.stratifiedSample(samples, requiredCountMap))


stratified sampling implementation:
1.数据分组：使用defaultdict将数据按label_col的值进行分组，每个标签对应一个列表，存放该类别的数据。
2.按比例抽样：计算每个类别在总数据中的比例，并按该比例抽取样本。
3.random.sample：从每个类别的数据列表中随机抽取样本

import random
from collections import defaultdict

def stratified_sampling(data, label_col, sample_size):
    """
    使用纯Python实现分层抽样
    :param data: list of dicts, 每个元素为一个包含数据和标签的字典，例如 [{'feature1': 1.2, 'label': 'A'}, ...]
    :param label_col: str, 类别标签所在的键名
    :param sample_size: int, 总样本数量
    :return: list of dicts, 抽取的样本
    """
    # 按照类别标签进行分组
    grouped_data = defaultdict(list)
    for item in data:
        grouped_data[item[label_col]].append(item)
    print(grouped_data)
    # 计算总数据量
    total_size = len(data)
    
    # 根据每个类别的比例计算抽样数，并从每个类别中随机抽取样本
    stratified_sample = []
    for label, items in grouped_data.items():
        # 计算该类别需要抽取的样本数量
        label_sample_size = int(len(items) / total_size * sample_size)
        # 随机抽取样本
        stratified_sample.extend(random.sample(items, label_sample_size))
    
    return stratified_sample

# 示例数据
data = [
    {'feature1': 1.2, 'label': 'A'},
    {'feature1': 2.3, 'label': 'B'},
    {'feature1': 0.4, 'label': 'A'},
    {'feature1': 1.5, 'label': 'C'},
    {'feature1': 1.7, 'label': 'B'},
    {'feature1': 3.1, 'label': 'C'},
    # 更多数据...
]

# 设定样本总量为3
sampled_data = stratified_sampling(data, label_col='label', sample_size=3)

print(sampled_data)
