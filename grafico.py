from matplotlib import pyplot as plt

def geraGraficoHistoricoFitness(historicoFitness):
    plt.plot(range(len(historicoFitness)), historicoFitness)
    plt.grid(True, zorder=0)
    plt.title("Ficticcia Transporte de Cargas")
    plt.xlabel("Geração")
    plt.ylabel("Valor médio carregado pelo caminhão")
    plt.show()