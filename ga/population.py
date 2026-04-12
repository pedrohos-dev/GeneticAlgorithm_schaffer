import numpy as np

def init_population(size):
    return np.random.uniform(-10, 10, (size, 2))