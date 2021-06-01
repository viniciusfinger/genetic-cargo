from Item import *
from tkinter import *
from json2html import *

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

def processaMelhorIndividuo(populacao, itens):
    cincoUltimosIndividuos = []
    indiceMelhorIndividuo = 0
    valorTotalMelhorIndividuo = 0
    for i in range(5):
        cincoUltimosIndividuos.append(populacao[i])
        valorTotalIndividuo = calculaValorTotal(populacao[i],itens)
        if valorTotalIndividuo > valorTotalMelhorIndividuo:
            valorTotalMelhorIndividuo = valorTotalIndividuo
            indiceMelhorIndividuo = i
    
    return populacao[indiceMelhorIndividuo]

def calculaValorTotal(individuo, itens):
    qtdItens = len(individuo)
    valorTotal = 0

    for i in range(qtdItens):
        if individuo[i] == 1:
            valorTotal += itens[i].getValor()
        
    return valorTotal

def processaTabelaHtmlItensIndividuo(individuo, itens): 
    i = 0
    objetos = []
    quantidadeCromossomos = len(individuo)

    while i < quantidadeCromossomos:
        if individuo[i] == 1:
            objetos.append(
                               {"nome":itens[i].getNome(),
                               "valor":itens[i].getValor(),
                                "peso":itens[i].getPeso()}
                             )
        i += 1
        
    html_file = open("tabela.html","w")
    tabelaHtml = json2html.convert(json=objetos)
    html_file.write(tabelaHtml)
    html_file.close()

    
