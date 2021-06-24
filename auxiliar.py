from Item import *
from tkinter import *
from json2html import *
import locale

def instanciaItens() -> list:
    itens = []

    itens.append(Item(nome="Escultura leao", peso=400, valor=1))
    itens.append(Item(nome="Escultura cisne", peso=700, valor=10000))
    itens.append(Item(nome="Escultura cristo", peso=2000, valor=500000))
    itens.append(Item(nome="Escultura cristo menor", peso=1000, valor=300000))
    itens.append(Item(nome="Escultura teste", peso=2000, valor=1000000))
    itens.append(Item(nome="Escultura vinicius finger", peso=100, valor=500000))
    itens.append(Item(nome="Escultura vinicius finger 2", peso=100, valor=500000))

    return itens

def geraTabelaConfiguracoes(capacidadeDeCarga, numeroDeIndividuos, geracoes):
    configuracoesJson = {"Capacidade de Carga":str(capacidadeDeCarga)+" kg","Número de Indivíduos":numeroDeIndividuos,"Número de Gerações":geracoes}

    html_file = open("tabelaConfiguracoes.html","w")
    tabelaConfiguracoes = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>'
    tabelaConfiguracoes += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">'
    tabelaConfiguracoes += json2html.convert(json=configuracoesJson,table_attributes='style="width: 100%;"')
  
    html_file.write(tabelaConfiguracoes)
    html_file.close()

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
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    objetos = []
    quantidadeCromossomos = len(individuo)
    valorTotal = 0
    pesoTotal = 0

    #Transforma os itens do indivíduo para um objeto JSON
    while i < quantidadeCromossomos:
        if individuo[i] == 1:
            valorTotal += itens[i].getValor()
            pesoTotal += itens[i].getPeso()
            objetos.append(
                               {"Nome":itens[i].getNome(),
                               "Valor":locale.currency(itens[i].getValor(), grouping=True),
                                "Peso":str(itens[i].getPeso())+" kg"}
                             )
        i += 1

    html_file = open("tabela.html","w")
    
    #Adiciona o bootstrap no frame HTML
    tabelaHtml = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>'
    tabelaHtml += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">'

    #Transforma o objeto JSON em uma tabela
    tabelaHtml += json2html.convert(json=objetos,table_attributes='style="width: 100%;"')
    
    html_file.write(tabelaHtml)
    html_file.close()

    objValorTotal = [{"Valor Total da Carga": locale.currency(valorTotal, grouping=True)}]
    
    html_file = open("tabela_valortotal.html","w")
    tabelaHtmlValorTotal = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>'
    tabelaHtmlValorTotal += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">'
    tabelaHtmlValorTotal += json2html.convert(json=objValorTotal,table_attributes='style="width: 100%;"')
    
    html_file.write(tabelaHtmlValorTotal)
    html_file.close()
