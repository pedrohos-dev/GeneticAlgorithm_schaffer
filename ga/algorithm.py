import numpy as np
from ga.population import init_population
from ga.selection import tournament_selection
from ga.crossover import arithmetic_crossover
from ga.mutation import mutate
from ga.fitness import evaluate

def genetic_algorithm(pop_size, generations, crossover_rate, mutation_rate):

    # população inicial
    pop = init_population(pop_size)

    # históricos
    best_history = []
    pop_history = []

    for gen in range(generations):

        # 1. Avalia população
        fitness = evaluate(pop)

        # 2. Salva população atual (para o vídeo)
        pop_history.append(pop.copy())

        # 3. Elitismo (pega o melhor da geração atual)
        best_idx = np.argmax(fitness)
        best_individual = pop[best_idx].copy()

        new_pop = []

        # 4. Parâmetros dinâmicos de mutação
        mutation_rate_dynamic = mutation_rate * (1 - gen / generations)
        sigma = 2 * (1 - gen / generations)

        # 5. Geração da nova população
        for _ in range(pop_size):

            # seleção
            p1 = tournament_selection(pop, fitness)
            p2 = tournament_selection(pop, fitness)

            # crossover
            if np.random.rand() < crossover_rate:
                child = arithmetic_crossover(p1, p2)
            else:
                child = p1.copy()

            # mutação
            child = mutate(child, mutation_rate_dynamic, sigma)

            new_pop.append(child)

        # 6. Aplica elitismo (garante que o melhor não se perde)
        new_pop[0] = best_individual

        # 7. Atualiza população
        pop = np.array(new_pop)

        # 8. Salva histórico do melhor fitness
        best = np.max(fitness)
        best_history.append(best)

        print(f"Geração {gen}; Fitness {best:.10f}")

    # salva população final também (opcional, mas útil pro vídeo)
    pop_history.append(pop.copy())

    return pop, best_history, pop_history