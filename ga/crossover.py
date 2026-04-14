import numpy as np

def arithmetic_crossover(p1, p2):
    # numero aleatorio entre 0 e 1
    alpha = np.random.rand()
    return alpha * p1 + (1 - alpha) * p2