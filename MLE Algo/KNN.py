from collections import Counter
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

class KNN:
    def __init__(self, k):
        self.k = k
    
    def fit(self, X, y):
        self.X_train = X 
        self.y_train = y
        
    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)
    
    def _predict(self, x):
        # distance between x and all training set example
        distances = [np.sqrt(np.sum((x - x_train)**2)) for x_train in X_train]
        
        # find nearest k indices (np.argsort(arr) return the ascending order index)
        k_indices = np.argsort(distances)[:self.k] 
        
        # get the labels of the k-nearest neighbors training samples
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # return the most common k samples(Counter.most_common(k) return top k frequent tuples: (key, freq))
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target 

# split training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

# train and predict
k = 3
knn = KNN(k = k)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# evaluate the classifier
accuracy = np.sum(y_pred == y_test) / len(y_test)


