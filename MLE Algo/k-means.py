import numpy as np
from matplotlib import pyplot as plt

# data[:,:]字面意思是[all_rows, all_cols], eg. [:,-1]表示所有行和最后一列
# np.random.randn(d0, d1...) 
# return n-dimention data with (0, 1) normal distribution -> res*sigma+mean可以return任意(mean,sigma)

# 1. Generate data
def data_generator():
  class1_data = np.random.randn(10, 2) + np.array([3,4])
  class2_data = np.random.randn(10, 2) + np.array([10,-4])
  class3_data = np.random.randn(10, 2) + np.array([-5, 0])
  return np.concatenate([class1_data, class2_data, class3_data], axis = 0)

# data = data_generator()
# plt.scatter(data[:,0], data[:,1])
# print(np.zeros(30))

# 2. kmeans
def kMeans(K, data, threshold = 1, max_iterations = 4):
  N = data.shape[0] #N = 30
  D = data.shape[1] #D = 2

  category = np.zeros(N) #the category of each data point 归属于K个centroid
  centroid = np.random.randn(K, D) # 初始化K个centroid

 
  for _ in range(max_iterations):

    # 1.计算每个样本到各个中心点的距离
    for i in range(N):
      min_distance = float("inf")
      for j in range(K):
        distance = np.linalg.norm(centroid[j] - data[i])

        # 2.根据距离最近的中心点将样本分配到对应的category(cluster)
        if distance < min_distance:
          min_distance = distance
          category[i] = j

    # 3. 更新中心点为每个cluster的平均值(update the centroid). 
    # eg. (0, 1),(1,2),(0,3) new_centroid for category 1 is (1/3, 2)

    new_centroid = np.array([data[category == k].mean(axis = 0) for k in range(K)])

    # 4.判断中心点是否converging，(multiple ways)
      # option 1: 直接更新旧的centroid作为新的
      # centroid = new_centroid

      # option 2: 计算diff小于threashold
    centroid_diff = np.linalg.norm(new_centroid - centroid)
    if centroid_diff < threshold:
      break
       # option 3: 
    if np.all(new_centroid == centroid):
      break
    
    centroid = new_centroid

    # graph
    plt.scatter(data[:,0], data[:,1], c = category) # c: color
    plt.plot(centroid[:,0], centroid[:,1], "r+")
    return category, centroid

#Test
if __name__ == "__main__":
  data = data_generator()
  K = 3
  kMeans(K, data)
    




