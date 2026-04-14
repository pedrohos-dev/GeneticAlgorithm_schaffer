import numpy as np

def schaffer(x, y):
    numerator = (np.sin(np.sqrt(x**2 + y**2)))**2 - 0.5
    denominator = (1 + 0.001*(x**2 + y**2))**2
    return 0.5 - (numerator / denominator)


# retorna um vetor com o fitness(schaffer) de cada individuo
def evaluate(pop):
    return np.array([schaffer(ind[0], ind[1]) for ind in pop])