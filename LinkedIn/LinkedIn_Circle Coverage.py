# given a random() which return floating number in [0, 1], 
# return a point(x, y) from a circle with radius R which return tuple(float, float)
# [rcos, rsin] -> R

import math
import random

def sampleFromCircle(R):
    theta = random * 2 * math.pi
    r = math.sqrt(random()) * R
    return (r * math.cos(theta), r*math.sin(theta))
            
            