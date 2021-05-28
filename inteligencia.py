from genetica import calculaMediaFitness, criaPopulacao
from dependencias import *

itens = instanciaItens()
capacidadeDeCarga = 100000000 #1 tonelada
numeroDeIndividuos = 150
geracoes = 5
numeroDeItens = len(itens)

populacao = criaPopulacao()

historicoFitness = [calculaMediaFitness(populacao, capacidadeDeCarga, itens)]

for geracao in range(geracoes):
    