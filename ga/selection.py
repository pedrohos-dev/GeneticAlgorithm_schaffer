import numpy as np

def tournament_selection(pop, fitness, k=2):
    idx = np.random.choice(len(pop), k)
    best = idx[np.argmax(fitness[idx])]
    return pop[best]