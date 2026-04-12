from ga.algorithm import genetic_algorithm
from ga.fitness import evaluate
from utils.plot import plot_fitness
import numpy as np

POP_SIZE = 50
GENERATIONS = 200
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.05

pop, history = genetic_algorithm(
    POP_SIZE,
    GENERATIONS,
    CROSSOVER_RATE,
    MUTATION_RATE
)

fitness = evaluate(pop)
best_idx = np.argmax(fitness)
best = pop[best_idx]

print("\nMelhor solução:")
print("x =", best[0])
print("y =", best[1])
print("fitness =", fitness[best_idx])

plot_fitness(history)