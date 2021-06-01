from genetica import *
from configs import *
from grafico import *
from auxiliar import processaMelhorIndividuo

populacao = criaPopulacao(numeroDeIndividuos, numeroDeItens)

#Calcula o primeiro fitness da população gerada aleatoriamente
historicoFitness = [calculaMediaFitness(populacao, capacidadeDeCarga, itens)]

#Evolui e calcula o fitness da população até acabar as gerações
for geracao in range(geracoes):
    populacao = evoluiPopulacao(populacao, capacidadeDeCarga, itens, numeroDeIndividuos)
    mediaFitnessPopulacao = calculaMediaFitness(populacao,capacidadeDeCarga,itens)
    historicoFitness.append(mediaFitnessPopulacao)

#Gera gráfico com histórico da média de fitness e valor total da carga do caminhão
geraGraficoHistoricoFitness(historicoFitness)

#Processa melhor indivíduo para JSON e abre a página HTML 
processaMelhorIndividuo(populacao, itens)
