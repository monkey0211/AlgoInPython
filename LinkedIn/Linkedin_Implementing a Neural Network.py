from math import exp
import random
from typing import List # 给bias node用

class Edge:
    def __init__(self, source:'Node', target: 'Node', weight: float):
        self.source = source
        self.target = target
        self.weight = weight
        self.source.outEdges.append(self)
        self.target.inEdges.append(self)
        
class Node:
    def __init__(self, index):
        self.index = index
        self.inEdges = [] # edges incoming
        self.outEdges = [] # edges outgoing
        
        self.cache = None # added later if needed.记录到当前点的 前向传播的值
        self.error = None # added later if needed.记录该点反向传播时的损失
        
        # add biasNode to every node if needed. -1 can be any value, 和正常node区别即可.
        self.inEdges.append(Edge(BiasNode(-1), self, random.uniform(0, 1))) 
    
    # need to add this helper
    def activation(self, x):
        return 1.0/(1.0 + exp(-x))
    
    # task1: 返回output layer values(can add cache later)
    # inputValues: dict[input node index] = input node value  
    def get_value(self, inputValues: dict[int, float]) -> float:
        # if self.cache:
        #     return self.cache
        
        if self.index in inputValues: #如果只有一层layer
            self.cache = inputValues[self.index]
        else:
            # 取出该点的所有入边 一个个算 w_i * x_i再累加起来->过activation
            total = 0
            for edge in self.inEdges:
                total += edge.weight * edge.source.get_value(inputValues)
            self.cache = self.activation(total)
                
        return self.cache

    # need to add clear cache later if needed. 
    def clear_cache(self):
        self.cache = None
        for edge in self.outEdges: # 把当前点的出边对应点清空?? TODO
            edge.target.clear_cache()
    
    # get the error of the node given the output node values
    # targetValues[output layer index] = output error
    # define loss?(需要问): 假设MSE的话 1/2*(target - output)^2 所以gradient/error is (target-output)
    def get_error(self, targetValues: dict[int, float]) -> float:
        #如果error已经有了 直接return
        if self.error:
            return self.error
        
        #如果已经是最后一层(或者只有一层targetValues) 直接计算error
        if self.index in targetValues:
            self.error = targetValues[self.index] - self.cache
        else:
            #每一层error需要weighted sum叠加: e(layer1的error) = w1e1 + w2e2(layer2的error)
            total_error = 0.0
            for e in self.outEdges:
                total_error += e.weight * e.target.get_error(targetValues)
            self.error = total_error
        return self.error     

    # 
   
    def update_weight(self, learningRate):
        
        # w(t) = w(t-1) + lr * dL/dw(t-1)
        # wx + b = p1 --> sigmoid(p1) --> p2 --> loss(p2, label)
        # 由链式法则: 总gradient: dL/dw = dL/dp2 * dp2/dp1 * dp1/dw  
        # dL/dp2: self.loss, 
        # dp2/dp1(sigmoid求导): self.cache * (1 - self.cache)
        # dp1/dw = x of input edge = edge.src.cache. 最后乘一个学习率lr
        for edge in self.inEdges:
            edge.weight += learningRate * self.error * self.cache * (1 - self.cache) * edge.source.cache
        
        
         # 也要更新出边 ??? TODO
        for edge in self.outEdges:
            edge.target.update_weight(learningRate)
                
class NeuralNetwork:
    def __init__(self, layers: List[int]): # layers[i]:第i层有多少个节点
        # 第一层input layer
        self.inputLayer = [Node(i) for i in range(layers[0])]
        offset = layers[0] #后续给Node编号用
        
        # 先记录下来前一层的节点
        preLayer = self.inputLayer 
        
        # 后面的layer: 1)创建每层layer的Node, 按顺序编号(offset_i) 2)用edge连接(preLayer, currLayer)
        for num in layers[1:]:
            currLayer = [Node(offset + i) for i in range(num)] # 给每一个node赋值
            offset += num
            for node1 in preLayer:
                for node2 in currLayer:
                    Edge(node1, node2)
            preLayer = currLayer
        self.outputLayer = preLayer 

    # output the value of output nodes given input nodes. 
    # 注意: 如果用cache的话 如果重复call会得到同一个结果, 所以需要先clear cache first. 
    def forward_pass(self, inputValues):
        self.clear() # clear cache
        res = {}
        for node in self.outputLayer:
            res[node.index] = node.get_value(inputValues)
        return res
        
    def clear(self):
        for node in self.inputLayer:
            node.clear_cache()
    
    # update weights
    # inputValues: a dictionary: input node index->input values
    # targetValues: a dictionary: output node index-> true label values
    def backward_pass(self, inputValues, targetValues, learningRate):
        self.forward_pass(inputValues)
        
        for node in self.inputLayer: #先收集所有点的loss
            node.get_error(targetValues)
        
        for node in self.inputLayer:
            node.update_weight(learningRate)
            
    
    # followup: support training this NN
    def train(self, samples):
        lr = 0.3 #learning rate
        epoch = 10000 # iteration
        decay_coeff = 0.99

        for i in range(epoch):
            for input, label in samples:
                self.backward_propagation(input, label, lr)
            lr = lr * decay_coeff # 更新learning rate. 每个epcho降低一次
        
# if need to add bias to node: create a biasNode, and incorporate into existing code
class BiasNode(Node):
    def __init__(self, index):
        self.index = index
        self.inEdges = []
        self.outEdges = []
        
        self.cache = 1
        self.error = None
    
    def get_value(self, inputValues):
        return 1  #??

    def get_error(self, label):
        for edge in self.outEdges: ## label?
            edge.target.get_error(label)
    
    
    def update_weight(self, learningRate):
        for edge in self.outEdges:
            edge.target.update_weight(learningRate)
    
    def clear_cache(self):
        self.error = None #?
        for edge in self.outEdges:
            edge.target.clear_cache()
    
    