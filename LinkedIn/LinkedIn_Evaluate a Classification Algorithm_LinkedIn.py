
import random
from typing import Dict, List
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score


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
    '''Evaluate a training algorithm'''
    
    # Shuffle the dataset
    random.shuffle(dataset)
    
    # Split the dataset into training and validation sets
    split_index = int(0.8 * len(dataset))
    train_data = dataset[:split_index]
    val_data = dataset[split_index:]
    
    # Train the classifier
    classifier = trainer.train(train_data)
    
    # Evaluate on validation set
    correct_predictions = 0
    for instance in val_data:
        features = instance.get_features()
        true_label = instance.get_label()
        predicted_label = classifier.classify(features)
        if predicted_label == true_label:
            correct_predictions += 1
    
    # Calculate accuracy
    accuracy = correct_predictions / len(val_data)
    
    return accuracy

# followup:
# 1. 怎样evaluate the model on the entire dataset(不是80 20): cross-validation
# 2. if instances are sorted by label, what could go wrong? a bias problem
# 3. if dataset is shuffled but no seed selected? result will vary and not stable 
# 4. if not use stratified sampling, label distribution is skewed? 一些folds里面no data of some specific label
# 5. what if labels are skewed? imbalance问题. 结果bias, poor performance on minority. 
    #做法: 调整class weight, over-sampling, 改用ensemble methods.  
    

# 改为k-folds(10-folds)方法
def evaluate(trainer: Trainer, dataset: List[LabelledInstance]) -> float:
    '''Evaluate a training algorithm using 10-fold cross-validation'''
    
    # Shuffle the dataset
    random.shuffle(dataset)
    
    # Perform 10-fold cross-validation
    fold_size = len(dataset) // 10
    total_accuracy = 0
    
    for i in range(10):
        # Split the dataset into training and validation sets
        start = i * fold_size
        end = start + fold_size
        val_data = dataset[start:end]
        train_data = dataset[:start] + dataset[end:]
        
        # Train the classifier
        classifier = trainer.train(train_data)
        
        # Evaluate on validation set
        correct_predictions = 0
        for instance in val_data:
            features = instance.get_features()
            true_label = instance.get_label()
            predicted_label = classifier.classify(features)
            if predicted_label == true_label:
                correct_predictions += 1
        
        # Calculate accuracy for this fold
        fold_accuracy = correct_predictions / len(val_data)
        total_accuracy += fold_accuracy
    
    # Calculate average accuracy across all folds
    average_accuracy = total_accuracy / 10
    
    return average_accuracy