from genetica import *
from configs import *


populacao = criaPopulacao(numeroDeIndividuos, numeroDeItens)

historicoFitness = [calculaMediaFitness(populacao, capacidadeDeCarga, itens)]

for geracao in range(geracoes):
    populacao = evoluiPopulacao(populacao, capacidadeDeCarga, itens, numeroDeIndividuos)
    mediaFitnessPopulacao = calculaMediaFitness(populacao,capacidadeDeCarga,itens)
    historicoFitness.append(mediaFitnessPopulacao)


#GERADOR DE GRAFICO
from matplotlib import pyplot as plt
plt.plot(range(len(historicoFitness)), historicoFitness)
plt.grid(True, zorder=0)
plt.title("Problema do caminhão")
plt.xlabel("Geração")
plt.ylabel("Valor médio carregado pelo caminhão")
plt.show()