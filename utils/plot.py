import matplotlib.pyplot as plt

def plot_fitness(history):
    plt.plot(history)
    plt.xlabel("Geração")
    plt.ylabel("Fitness")
    plt.title("Evolução do AG")
    plt.show()