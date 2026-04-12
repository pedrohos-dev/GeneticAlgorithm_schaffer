import numpy as np

def mutate(ind, rate=0.05):
    if np.random.rand() < rate:
        ind += np.random.normal(0, 0.5, size=2)
    return np.clip(ind, -10, 10)