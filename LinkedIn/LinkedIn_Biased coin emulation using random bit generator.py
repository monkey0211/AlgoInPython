# given system method that generates random bits uniformly
# create a function that emulates biased coin, with given probability.
# precision is within 10e-2
import random

def generateBiasedCoinUsingBitRandomNumber(prob):
    precision = 1e-2  # Desired precision

    rand_num = 0
    factor = 0.5
    while rand_num < 1 - precision:
        rand_num += factor * random.choice([0, 1])
        factor *= 0.5 #类似decision tree, 需要知道下一步+-0.5/0.25/0.125...
       
    if rand_num < prob:
        return 1  # Head (biased towards 1 with probability 'prob')
    else:
        return 0  # Tail

# test
prob = 0.7
heads_count = 0
tails_count = 0
trials = 10000

for _ in range(trials):
    if generateBiasedCoinUsingBitRandomNumber(prob) == 1:
        heads_count += 1
    else:
        tails_count += 1