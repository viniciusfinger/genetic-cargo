from auxiliar import instanciaItens, geraTabelaConfiguracoes

capacidadeDeCarga = 4000 #kg
numeroDeIndividuos = 150
geracoes = 100
itens = instanciaItens() #Instancia os itens disponíveis para serem carregados
numeroDeItens = len(itens)

#Gera tabela com as informações de configurações para exibição na tela final
geraTabelaConfiguracoes(capacidadeDeCarga, numeroDeIndividuos, geracoes)