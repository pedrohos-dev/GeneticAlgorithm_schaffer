import numpy as np
from ga.population import init_population
from ga.selection import tournament_selection
from ga.crossover import arithmetic_crossover
from ga.mutation import mutate
from ga.fitness import evaluate

def genetic_algorithm(pop_size, generations, crossover_rate, mutation_rate):

    pop = init_population(pop_size)
    best_history = []

    for gen in range(generations):

        fitness = evaluate(pop)
        new_pop = []

        for _ in range(pop_size):
            p1 = tournament_selection(pop, fitness)
            p2 = tournament_selection(pop, fitness)

            if np.random.rand() < crossover_rate:
                child = arithmetic_crossover(p1, p2)
            else:
                child = p1.copy()

            child = mutate(child, mutation_rate)
            new_pop.append(child)

        pop = np.array(new_pop)

        best = np.max(fitness)
        best_history.append(best)

        print(f"Geração {gen}: {best:.6f}")

    return pop, best_history