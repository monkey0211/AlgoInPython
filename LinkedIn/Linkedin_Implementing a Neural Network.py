from math import exp
import random

class Edge:
    def __init__(self, source, target, weight):
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
        
        self.cache = None # added later if needed
        self.error = None # added later if needed
        
        # add biasNode to every node if needed. -1 can be any value, 和正常node区别即可.
        self.inEdges.append(Edge(BiasNode(-1), self, random.uniform(0, 1))) 
    
    # need to add this helper
    def activation(self, x):
        return 1.0/(1.0 + exp(-x))
    
    # task1: get the output layer values(can add cache later)
    # inputValues: dict[input node index] = input node value  
    def get_value(self, inputValues):
        # if self.cache:
        #     return self.cache
        
        if self.index in inputValues: #如果只有一层layer
            self.cache = inputValues[self.index]
        else:
            total = 0
            for edge in self.inEdges:
                total += edge.weight * edge.source.get_value(inputValues)
            self.cache = self.activation(total)
                
            # self.cache = self.activation(sum([e.weight * e.source.get_value(inputValues) for e in self.inEdges]))
        return self.cache

    # need to add clear cache later if needed. 
    def clear_cache(self):
        self.cache = None
        for edge in self.outEdges:
            edge.target.clear_cache()
    
    # get the error of the node given the output node values
    # targetValues[output layer index] = output error
    # define loss: 1/2*(target - output)^2 所以gradient/error is (target-output)
    def get_error(self, targetValues):
        #如果error已经有了 直接return
        if self.error:
            return self.error
        
        #如果已经是最后一层(或者只有一层targetValues) 直接计算error
        if self.index in targetValues:
            self.error = targetValues[self.index] - self.cache
        else:
            #每一层error需要weighted sum叠加: e(layer1的error) = w1e1 + w2e2(layer2的error)
            total_error = 0 
            for e in self.outEdges:
                total_error += e.weight * e.target.get_error(targetValues)
            self.error = total_error
        return self.error     

    # learningRate: learning rate
    def update_weight(self, learningRate):
        for edge in self.inEdges:
            edge.weight += learningRate * self.error * self.cache * (1 - self.cache) * edge.source.cache
        for edge in self.outEdges:
            edge.target.update_weight(learningRate)
                
class NeuralNetwork:
    def __init__(self, layers):
        '''layers: a list containing the number of nodes in each layer. 
        The first layer is input layer and the last layer is the output layer'''
        self.inputLayer = [Node(i) for i in range(layers[0])]
        ind = layers[0]
        pre = self.inputLayer # 先记录下来input layer. 
        for num in layers[1:]:
            layer = [Node(ind + i) for i in range(num)]
            ind += num
            for node1 in pre:
                for node2 in layer:
                    Edge(node1, node2, random.uniform(0, 1))
            pre = layer
        self.outputLayer = pre 

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
        
        for node in self.inputLayer:
            node.get_error(targetValues)
        
        for node in self.inputLayers:
            node.update_weight(learningRate)
            
    
        
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
    
    