
from typing import Dict, List
import random

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


'''
下面这一版 实现了:
1. stratified k fold: 确保每个fold中各个类别的比例与整个数据集相似
2. 多个评估指标:准确率、精确率、召回率和F1分数。这些能更全面地反映模型在不平衡数据集上的表现。
3. 返回一个包含所有2中指标的dict 而不是单一的float值 可以提供更全面的评估结果
'''
from collections import defaultdict

def stratified_k_fold(dataset, k=10):
    # Group instances by label
    label_to_instances = defaultdict(list)
    for instance in dataset:
        label_to_instances[instance.get_label()].append(instance)
    
    # Create stratified folds
    folds = [[] for _ in range(k)]
    for instances in label_to_instances.values():
        for i, instance in enumerate(instances):
            folds[i % k].append(instance)
    
    return folds

def calculate_metrics(y_true, y_pred):
    tp = sum((t == p == 1) for t, p in zip(y_true, y_pred))
    fp = sum((t == 0 and p == 1) for t, p in zip(y_true, y_pred))
    fn = sum((t == 1 and p == 0) for t, p in zip(y_true, y_pred))
    tn = sum((t == p == 0) for t, p in zip(y_true, y_pred))
    
    accuracy = (tp + tn) / (tp + tn + fp + fn) if tp + tn + fp + fn > 0 else 0
    precision = tp / (tp + fp) if tp + fp > 0 else 0
    recall = tp / (tp + fn) if tp + fn > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }

def evaluate(trainer: Trainer, dataset: List[LabelledInstance]) -> dict:
    '''Evaluate a training algorithm using stratified 10-fold cross-validation'''
    
    folds = stratified_k_fold(dataset, k=10)
    all_metrics = defaultdict(list)
    
    for i in range(10):
        val_data = folds[i]
        train_data = [instance for j, fold in enumerate(folds) if j != i for instance in fold]
        
        classifier = trainer.train(train_data)
        
        y_true = []
        y_pred = []
        for instance in val_data:
            features = instance.get_features()
            true_label = instance.get_label()
            predicted_label = classifier.classify(features)
            y_true.append(true_label)
            y_pred.append(predicted_label)
        
        fold_metrics = calculate_metrics(y_true, y_pred)
        for metric, value in fold_metrics.items():
            all_metrics[metric].append(value)
    
    # Calculate average metrics across all folds
    avg_metrics = {metric: sum(values) / len(values) for metric, values in all_metrics.items()}
    
    return avg_metrics