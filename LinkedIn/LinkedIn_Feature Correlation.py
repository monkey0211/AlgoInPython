# given: featureVal - response. 分布不均匀 如何分桶
# 如何知道这个feature是否对reponse有影响/is it ok to use the feature as it is?: 
# 1) scatter plot.适用于少量数据. plt.scatter(x, y)
# density of 0s is high when featureVal is low and 1's density high when featureVal is high
# 2)bucketize. 不可以max-min区间平均分(有的bucket数据点多 有的很少)
# 如何分桶: 按percentile算, 每个percentile算一个桶, 这样可以避免分配不均匀的问题
# 然后每个桶计算 x=avg(inputValue) -> y=avg(response)

import math

class Sample:
    def __init__(self, feature, response):
        self.feature = feature
        self.response = response
    def __lt__(self, other):
        return self.feature < other.feature
# input: samples, 
# output: a list of 100 points(buckets, avg)
def getBucketizedFeature(samples):
    # sample sorting
    samples.sort(key = lambda x: x.feature)
    # how many data in one bucket
    bucketSize = math.ceil(len(samples)/ 10.0) #如果每一个percentile作为一个桶
    
    featureTotal = 0
    responseTotal = 0
    cnt = 0
    sampleList = []
    for sample in samples:
        featureTotal += sample.feature
        responseTotal += sample.response
        cnt += 1
        if cnt == bucketSize:
            # 新创建一个点: feature, response分别取平均
            avgSample = Sample(featureTotal/cnt, responseTotal/cnt)
            sampleList.append(avgSample)
            featureTotal = 0
            responseTotal = 0
            cnt = 0
    # 可能还有剩余data(因为每个bucket都是ceil可能多装)
    if cnt != 0:
        avgSample = Sample(featureTotal/cnt, responseTotal/cnt)
        sampleList.append(avgSample)
    
    return sampleList 
        
# followup:
# suggest a suitable feature transformation? Linear spline transformation
# 1.预测结果不好原因? 1)large variance per bucket. 2)correlation with existing features.  
# 2.if logisitic: response用log of average response.  
# 3.if data too large to fit into a single machine: TODO
    # 1.map-reduce to sort. 
    # 2.compute percentiles to get 100 buckets boundary value.
    # 3. for each data point, 找到对应的bucket
    # 4. calculate average feature and response. 
     
            
        
s1 = Sample(0.1, 1)  
s2 = Sample(0.2, 0)  
s3 = Sample(0.5, 1)  
s4 = Sample(0.2, 0) 
samples = [s1,s2,s3,s4]
res = getBucketizedFeature(samples)
for i in range(len(res)):
    print(res[i].feature, res[i].response)
        
        
    