from matplotlib import pyplot as plt

def generate_fitness_history_chart(historicoFitness):
    plt.plot(range(len(historicoFitness)), historicoFitness)
    plt.grid(True, zorder=0)
    plt.title("Evolução do valor total conforme as gerações")
    plt.xlabel("Geração")
    plt.ylabel("Valor médio carregado pelo caminhão (R$)")

    plt.savefig('./web/grafico.png')

