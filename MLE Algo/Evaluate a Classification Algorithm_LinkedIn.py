from typing import Dict, List
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


FeatureMap = Dict[str, float]
class LabelledInstance:
    # a feature vector and its label
    def get_features(self) -> FeatureMap:
        pass 
    def get_label(self) -> int: 
        pass

class Classifier:
    # a classifier predicting a label from a feture vector
    def classify(self, instance: FeatureMap) -> int:
        pass

class Trainer:
    # an algorithm to train a Classifier
    def train(self, dataset: List[LabelledInstance]) -> Classifier:
        pass

def evaluate(trainer: Trainer, dataset: List[LabelledInstance]) -> float:
    '''write a method to evaluate a training algorithm'''
    
    features = [d.get_features() for d in dataset]
    labels = [d.get_label() for d in dataset]
    
    
    X_train, X_val, y_train, y_val = train_test_split(features, labels, test_size=0.2, random_state=42)
    
    # train the model
    clf = trainer.train(X_train, y_train)
    
    # predict
    y_pred = clf.classify(X_val)
    
    #Evaluate the model: AUC, ROC, etc.
    accuracy = accuracy_score(y_val, y_pred)
    report = classification_report(y_val, y_pred)
    return accuracy, report
    