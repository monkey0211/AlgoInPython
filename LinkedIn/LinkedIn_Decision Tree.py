
import math
from typing import List, Set


class Feature:
    def __init__(self, name: str = "", val: bool = False):
        self.name = name 
        self.val = val
    def __eq__(self, other):
        if isinstance(other, Feature):
            return self.name == other.name
        return False
    def __hash__(self):
        return hash(self.name)
    
class Instance:
    #优化点: features用set不是list: assume所有的features都是binary, 只需要把positive的feature放入set. 节省空间
    def __init__(self, features: Set[Feature] = set(), label:bool = False):
        self.features = features
        self.label = label

# decision tree node definition
class Node:
    def __init__(self, left:'Node' = None, right:'Node' = None, feature:Feature = None):
        self.left = left
        self.right = right
        self.feature = feature # feature on which we split a tree-node

# 主要function: create a descision tree and do recursion.

def createDecisionTree(instances, features):
    if not instances or not features:
        return None
    # base case: 已经hit leaf node, 直接返回一个空root即可
    # terminate condition: 需要讨论如何结束, 这里假设如果所有instance的label值只有一个(pure)就可以terminate
    if hitTerminationCondition(instances):
        return Node()
    
    # 1.计算每个feature的gain, 返回max gain的feature
    maxGainFeature = getMaxGainFeature(instances, features)
    
    # 2.用maxGainFeature作为target feature, split tree: left tree & right tree
    leftInstances, rightInstances = splitInstances(instances, maxGainFeature)
    
    # optimization:
    # 如果是binary label, 每个feature只会split一次 所以用过之后可以从set里除去 不会再用
    # it doesn't apply for dense features (dense means continuous) 
    features.remove(maxGainFeature)
    
    # recursion
    leftNode = createDecisionTree(leftInstances, features)
    rightNode = createDecisionTree(rightInstances, features)
    
    return Node(leftNode, rightNode, maxGainFeature)

# 返回最大的information gain的一个feature
def getMaxGainFeature(instances, features):
    maxGain = 0
    res = None
    for feature in features:
        gain = computeInformationGain(instances, feature)
        if gain > maxGain:
            maxGain = gain
            res = feature
    return res

# split instances into two lists: left是不包含targetFeature的sample list, right是包含
def splitInstances(instances, targetFeature):
    left, right = [], []
    for ins in instances:
        if targetFeature in ins.features:
            right.append(ins)
        else:
            left.append(ins)
    return left, right

# 当instances里面所有label都一样时 可以结束split: 
# 用一个set装所有的label值(0 or 1). set里面就只有一个值 return True
def hitTerminationCondition(instances:List[Instance]) -> bool:
    keySet = set()
    for ins in instances:
        keySet.add(ins.label)
    return len(keySet) == 1

# compute information gain: 
# gain = parent entropy - weighted avg of the child node's entropy
def computeInformationGain(instances:List[Instance], feature:Feature) -> Feature:
    entropy = calculateEntropy(instances, feature)  # current parent entropy
    
    # children nodes
    leftInstances, rightInstances = splitInstances(instances, feature)
    leftEntropy = calculateEntropy(leftInstances, feature)
    rightEntropy = calculateEntropy(rightInstances, feature)
    
    leftWeight = len(leftInstances) / len(instances)
    rightWeight = len(rightInstances) / len(instances)
    
    # parent entropy - weighted children entropy
    return entropy - leftWeight * leftEntropy - rightWeight * rightEntropy


# entropy = -(p*ln(p) + (1-p)*ln(1-p))
# p is probability that the bool type feature equals to 1
def calculateEntropy(instances, feature):
    # 计算这个feature为1
    cnt = 0
    for ins in instances:
        if feature in ins.features:
            cnt += 1
    prob = cnt / len(instances) # feature出现的概率
    return -(prob*math.log(prob) + (1-prob) * math.log((1-prob)))

    
    
