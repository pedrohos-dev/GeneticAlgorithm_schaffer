import numpy as np

def schaffer(x, y):
    num = np.sin(np.sqrt(x**2 + y**2))**2 - 0.5
    den = (1 + 0.001*(x**2 + y**2))**2
    return 0.5 - (num / den)

def evaluate(pop):
    return np.array([schaffer(ind[0], ind[1]) for ind in pop])