# reservoir sampling
# input: billions of training examples in a file, each has one of 4 class labels. 
# output: select M random samples from each class c={1,2,3,4}

class Example:
    def __init(self, label):
        self.label = label

    def stratifiedSample(examples, samplesRequiredMap):
        