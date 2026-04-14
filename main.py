import numpy as np
from ga.algorithm import genetic_algorithm
from ga.fitness import evaluate
from utils.plot import plot_fitness
from utils.video import generate_video

# ==============================
# Parâmetros do algoritmo
# ==============================
POP_SIZE = 30
GENERATIONS = 100
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.15

# ==============================
# Executa o algoritmo genético
# ==============================
pop, history, pop_history = genetic_algorithm(
    POP_SIZE,
    GENERATIONS,
    CROSSOVER_RATE,
    MUTATION_RATE
)

# ==============================
# Melhor solução encontrada
# ==============================
fitness = evaluate(pop)
best_idx = np.argmax(fitness)
best = pop[best_idx]

print("\nMelhor solução encontrada:")
print(f"x = {best[0]}")
print(f"y = {best[1]}")
print(f"fitness = {fitness[best_idx]}")

# ==============================
# Gráfico da evolução
# ==============================
plot_fitness(history)

# ==============================
# Geração do vídeo
# ==============================
print("\nGerando vídeo da evolução...")
generate_video(pop_history)

print("Vídeo gerado com sucesso!")