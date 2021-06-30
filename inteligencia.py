from dashboard import abreDashboard
from genetica import *
from configs import *
from web.grafico import *
from auxiliar import processaMelhorIndividuo, processaTabelaHtmlItensIndividuo

#Cria a população inicial de forma psuedo-aleatória
populacao = criaPopulacao(numeroDeIndividuos, numeroDeItens)

#Calcula o primeiro fitness da população 
historicoFitness = [calculaMediaFitness(populacao, capacidadeDeCarga, itens)]

#Evolui, calcula e guarda o fitness da população até acabar as gerações
for geracao in range(geracoes):
    populacao = evoluiPopulacao(populacao, capacidadeDeCarga, itens, numeroDeIndividuos)
    mediaFitnessPopulacao = calculaMediaFitness(populacao,capacidadeDeCarga,itens)
    historicoFitness.append(mediaFitnessPopulacao)

#Gera gráfico em PNG com histórico da média de fitness e valor total da carga do caminhão
geraGraficoHistoricoFitness(historicoFitness)

#Processa o melhor indivíduo, seu set de itens e processa e abre a página HTML 
melhorIndividuo = processaMelhorIndividuo(populacao, itens)
processaTabelaHtmlItensIndividuo(melhorIndividuo, itens)

abreDashboard()
