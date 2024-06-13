import numpy as np
import seaborn as sns 
# sigmoid = expX/(1+expX)
def sigmoid(x):
    exp_x = np.exp(x) #np.exp(array) returns array
    return exp_x/(1+exp_x) # or np.divide(exp_x, (1+exp_x))

# Test
x = np.linspace(-10, 10, num = 200) # return evenly spaced numbers in a range
sigmoidArray = sigmoid(x)

#graph
sns.lineplot(x=x, y = sigmoidArray).set(title = "sigmoid Function")


#input: array Z. output: probability array after softmax
def softmax(z):
    exp_z = np.exp(z)
    sum = exp_z.sum()
    return np.round(exp_z/sum, 3)

#Test
array = [0.25, 1,23, -0.8]
print(softmax(array))