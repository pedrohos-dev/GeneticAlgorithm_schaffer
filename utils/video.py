import numpy as np
import matplotlib.pyplot as plt
import imageio

# ==============================
# Função de Schaffer
# ==============================
def schaffer(x, y):
    num = (np.sin(np.sqrt(x**2 + y**2)))**2 - 0.5
    den = (1 + 0.001*(x**2 + y**2))**2
    return 0.5 - (num / den)

# ==============================
# Geração do vídeo (~10 segundos)
# ==============================
def generate_video(pop_history, filename="evolucao.gif"):

    frames = []

    total_generations = len(pop_history)

    # queremos ~100 frames no máximo
    max_frames = 100
    step = max(1, total_generations // max_frames)

    # fps pra dar ~10 segundos
    fps = max(5, len(range(0, total_generations, step)) // 10)

    # grade para curvas de nível
    x = np.linspace(-10, 10, 200)
    y = np.linspace(-10, 10, 200)
    X, Y = np.meshgrid(x, y)
    Z = schaffer(X, Y)

    for gen in range(0, total_generations, step):

        pop = pop_history[gen]

        plt.figure(figsize=(6, 6))

        # fundo (curvas)
        plt.contourf(X, Y, Z, levels=30, alpha=0.7)

        # população
        xs = pop[:, 0]
        ys = pop[:, 1]

        plt.scatter(
            xs, ys,
            c='white',
            s=40,
            edgecolors='black',
            zorder=3
        )

        # melhor indivíduo
        fitness = schaffer(xs, ys)
        best_idx = np.argmax(fitness)

        plt.scatter(
            xs[best_idx], ys[best_idx],
            c='yellow',
            s=80,
            edgecolors='black',
            zorder=4
        )

        # configurações
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.title(f"Geração {gen}")
        plt.xlabel("x")
        plt.ylabel("y")

        # salva frame
        plt.savefig("temp.png")
        plt.close()

        frames.append(imageio.imread("temp.png"))

    # gera GIF (~10 segundos)
    imageio.mimsave(filename, frames, fps=fps)

    print(f"Vídeo gerado com ~10s: {filename}")