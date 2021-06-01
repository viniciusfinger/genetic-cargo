from auxiliar import instanciaItens
from json2html import *

capacidadeDeCarga = 4000 #kg
numeroDeIndividuos = 100
geracoes = 100
itens = instanciaItens()
numeroDeItens = len(itens)

configuracoesJson = {"Capacidade de Carga":str(capacidadeDeCarga)+" kg","Número de Indivíduos":numeroDeIndividuos,"Número de Gerações":geracoes}

html_file = open("tabelaConfiguracoes.html","w")
tabelaConfiguracoes = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>'
tabelaConfiguracoes += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">'
tabelaConfiguracoes += json2html.convert(json=configuracoesJson,table_attributes='style="width: 100%;"')
  
html_file.write(tabelaConfiguracoes)
html_file.close()