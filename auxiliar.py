from Item import *
from tkinter import *

def instanciaItens() -> list:
    itens = []

    itens.append(Item(nome="Escultura leao", peso=400, valor=0.1))
    itens.append(Item(nome="Escultura cisne", peso=700, valor=10000))
    itens.append(Item(nome="Escultura cristo", peso=2000, valor=500000))
    itens.append(Item(nome="Escultura cristo menor", peso=1000, valor=300000))
    itens.append(Item(nome="Escultura teste", peso=2000, valor=1000000))
    itens.append(Item(nome="Escultura vinicius finger", peso=100, valor=500000))
    itens.append(Item(nome="Escultura vinicius finger 2", peso=100, valor=500000))

    return itens

def printaMelhorIndividuo(populacao, itens):
    cincoUltimosIndividuos = []
    indiceMelhorIndividuo = 0
    valorTotalMelhorIndividuo = 0
    for i in range(5):
        cincoUltimosIndividuos.append(populacao[i])
        valorTotalIndividuo = calculaValorTotal(populacao[i],itens)
        if valorTotalIndividuo > valorTotalMelhorIndividuo:
            valorTotalMelhorIndividuo = valorTotalIndividuo
            indiceMelhorIndividuo = i

    printaItensMelhorIndividuo(populacao[indiceMelhorIndividuo], itens)


def calculaValorTotal(individuo, itens):
    qtdItens = len(individuo)
    valorTotal = 0

    for i in range(qtdItens):
        if individuo[i] == 1:
            valorTotal += itens[i].getValor()
        
    return valorTotal


def printaItensMelhorIndividuo(individuo, itens): 
    root = Tk()
    i = 0
    quantidadeCromossomos = len(individuo)
    valorTotal = 0

    while i < quantidadeCromossomos:
        if individuo[i] == 1:
            valorTotal += itens[i].getValor()
            print(itens[i].getNome() +" " +str(itens[i].getPeso())+"kg " + "R$"+str(itens[i].getValor()))
        i += 1

    print("Valor total do melhor indivíduo: R$" + str(valorTotal))