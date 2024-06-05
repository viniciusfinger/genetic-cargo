from Item import *
from tkinter import *
from json2html import *
import locale

def instanciaItens() -> list:
    itens = []

    itens.append(Item(name="Cadeira", weight=15, price=1500))
    itens.append(Item(name="Celular top", weight=0.8, price=8700))
    itens.append(Item(name="Notebook", weight=3, price=4000))
    itens.append(Item(name="Piano Yamaha", weight=250, price=250000))
    itens.append(Item(name="Piano Roch", weight=250, price=250000))
    itens.append(Item(name="Televisão 50 pol.", weight=12, price=3000))
    itens.append(Item(name="Televisão 22 pol.", weight=8, price=999))
    itens.append(Item(name="Cama king", weight=100, price=20000))
    itens.append(Item(name="Sofá", weight=120, price=7000))
    itens.append(Item(name="Kit academia", weight=500, price=15000))
    itens.append(Item(name="Escultura de gesso", weight=500, price=10000))
    itens.append(Item(name="Escultura Tigresa", weight=300, price=87000))
    itens.append(Item(name="Escultura de mármore", weight=700, price=90000))
    itens.append(Item(name="Geladeira top", weight=125, price=10000))
    itens.append(Item(name="Geladeira", weight=90, price=2500))
    itens.append(Item(name="Freezer", weight=90, price=3500))
    itens.append(Item(name="Fogão a lenha n3", weight=100, price=3500))
    itens.append(Item(name="Esteira", weight=130, price=2500))
    itens.append(Item(name="Mesa tampo de mármore 6 cadeiras", weight=100, price=8000))
    itens.append(Item(name="Livro", weight=0.3, price=35))
    itens.append(Item(name="Jogo 4 pneus", weight=45, price=2500))
    itens.append(Item(name="Quadro", weight=45, price=5000))
    itens.append(Item(name="Kit anilhas", weight=450, price=2000))
    itens.append(Item(name="2000kg de tinta", weight=2000, price=20000))


    return itens

def generate_config_table(load_capacity, individuals_number, generations):
    configuracoesJson = {"Capacidade de Carga":str(load_capacity)+" kg","Número de Indivíduos":individuals_number,"Número de Gerações":generations}

    html_file = open("tabelaConfiguracoes.html","w")
    tabelaConfiguracoes = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>'
    tabelaConfiguracoes += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">'
    tabelaConfiguracoes += json2html.convert(json=configuracoesJson,table_attributes='style="width: 100%;"')
  
    html_file.write(tabelaConfiguracoes)
    html_file.close()

def get_best_individual(population, items):
    five_last_individuals = []
    best_individual_index = 0
    best_individual_value = 0
    for i in range(5):
        five_last_individuals.append(population[i])
        invidual_total_value = calculate_total_value(population[i], items)
        if invidual_total_value > best_individual_value:
            best_individual_value = invidual_total_value
            best_individual_index = i
    
    return population[best_individual_index]

def calculate_total_value(individual, items):
    item_quantity = len(individual)
    total_value = 0

    for i in range(item_quantity):
        if individual[i] == 1:
            total_value += items[i].getValor()
        
    return total_value

def generate_html_individual_items(individual, items): 
    i = 0
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    objetos = []
    chromossomes_quantity = len(individual)
    valorTotal = 0
    pesoTotal = 0

    #Transforma os itens do indivíduo para um objeto JSON
    while i < chromossomes_quantity:
        if individual[i] == 1:
            valorTotal += items[i].getValor()
            pesoTotal += items[i].getPeso()
            objetos.append(
                               {"Nome":items[i].getNome(),
                               "Valor":locale.currency(items[i].getValor(), grouping=True),
                                "Peso":str(items[i].getPeso())+" kg"}
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

    objValorTotal = [{"Valor Total da Carga": locale.currency(valorTotal, grouping=True),
                      "Peso Total da Carga:": round(pesoTotal, 2)
                    }]
    
    html_file = open("tabela_valortotal.html","w")
    tabelaHtmlValorTotal = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>'
    tabelaHtmlValorTotal += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">'
    tabelaHtmlValorTotal += json2html.convert(json=objValorTotal,table_attributes='style="width: 100%;"')
    
    html_file.write(tabelaHtmlValorTotal)
    html_file.close()
