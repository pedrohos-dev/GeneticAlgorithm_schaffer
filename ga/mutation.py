import numpy as np

def mutate(ind, rate, sigma):
    for i in range(len(ind)):  # percorre x e y
         # faz um sorteio se vai mutar ou nao
        if np.random.rand() < rate:
            ind[i] += np.random.normal(0, sigma)  # mutação mais forte
    
    return np.clip(ind, -10, 10)