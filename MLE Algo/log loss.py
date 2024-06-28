def logLoss(y_true, y_pred):
    score = y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)
    return -score / len(y_true)