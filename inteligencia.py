from genetica import *
from configs import *
from grafico import *


populacao = criaPopulacao(numeroDeIndividuos, numeroDeItens)

historicoFitness = [calculaMediaFitness(populacao, capacidadeDeCarga, itens)]

for geracao in range(geracoes):
    populacao = evoluiPopulacao(populacao, capacidadeDeCarga, itens, numeroDeIndividuos)
    mediaFitnessPopulacao = calculaMediaFitness(populacao,capacidadeDeCarga,itens)
    historicoFitness.append(mediaFitnessPopulacao)

#Gera gráfico com histórico da média de fitness e valor total da carga do caminhão
geraGraficoHistoricoFitness(historicoFitness)