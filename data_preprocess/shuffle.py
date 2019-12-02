import numpy as np

def shuffle(X,Y,seed):
    np.random.seed(seed)
    randomList = np.arange(X.shape[0])
    np.random.shuffle(randomList)
    return X[randomList], Y[randomList]
