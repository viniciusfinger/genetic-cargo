from random import getrandbits, random, randint

def criaIndividuo(numeroDeItens):
    """
    Gera um array chamado indivíduo (cromossomos), onde cada posição desse array 
    representa um item que caso estiver com 1 no valor será levado no caminhão 
    e 0 não será levado.
    """
    individuo = [getrandbits(1) for x in range(numeroDeItens)]
    return individuo

def criaPopulacao(numeroDeIndividuos, numeroDeItens):
    #Cria a populacao de individuos
    populacao = [criaIndividuo(numeroDeItens) for x in range(numeroDeIndividuos)]
    return populacao

def calculaMediaFitness(populacao, pesoMaximo, itens):
    #Calcula a avaliação media da população de indivíduos
    somatorio = sum(calculaFitness(individuo, pesoMaximo, itens) for individuo in populacao if calculaFitness(individuo, pesoMaximo, itens) >= 0)
    mediaFitness = somatorio / (len(populacao) * 1.0)
    
    return mediaFitness

def calculaFitness(individuo, capacidadeDeCarga, itens):
    #Faz a avaliação de um único indivíduo
    pesoTotal = 0
    valorTotal = 0

    for indiceItem in individuo:
        pesoTotal = pesoTotal + (individuo[indiceItem] * itens[indiceItem].getPeso())
        valorTotal = valorTotal + (individuo[indiceItem] * itens[indiceItem].getValor())

        if (capacidadeDeCarga - pesoTotal) < 0:
            return -1 #Peso total do caminhão excedido.
        else:
            return valorTotal
    
def evoluiPopulacao(populacao, capacidadeDeCarga, itens, numeroDeIndividuos, mutacao=0.05):
    #Classifica o fitness e seu respectivo indivíduo em um array
    pais = [[calculaFitness(individuo, capacidadeDeCarga, itens), individuo] for individuo in populacao if calculaFitness(individuo,capacidadeDeCarga, itens) >= 0]
    pais.sort(reverse=True)

    #Reprodução dos indivíduos
    filhos = []

    while len(filhos) < numeroDeIndividuos:
        pai, mae = sorteiaPais(pais)
        meioDoCromossomo = len(pai) // 2

        #Filho vai ser a primeira metade do pai + a primeira metade da mãe
        filho = pai[:meioDoCromossomo] + mae [meioDoCromossomo:]
        filhos.append(filho)

    #Faz a mutação em um cromossomo do indivíduo
    for filho in filhos:
        if mutacao > random():
            cromossomoASerMutado = randint(0, len(filho)-1)

            if filho[cromossomoASerMutado] == 1:
                filho[cromossomoASerMutado] = 0
            else:
                filho[cromossomoASerMutado] = 1
    
    return filhos

def sorteiaPais(pais):
    #Sorteia um pai e uma mãe baseado na regra da roleta

    def sorteiaIndice(fitnessTotal, indiceIgnorado =-1):
        #Indice ignorado = indice do pai, para não ser sorteado de novo.

        roleta = []
        acumulado = 0
        valorSorteado = random()

        if indiceIgnorado != -1:
            fitnessTotal -= valores[0][indiceIgnorado]        
        
        for indice, i in enumerate(valores[0]):
            if indiceIgnorado == indice:
                continue
            acumulado += i
            roleta.append(acumulado/fitnessTotal)

            if roleta[-1] >= valorSorteado:
                return indice
    
    #Cria duas listas com os valores de fitness e indivíduos
    valores = list(zip(*pais))
    fitnessTotal = sum(valores[0])

    indicePai = sorteiaIndice(fitnessTotal)
    indiceMae = sorteiaIndice(fitnessTotal, indicePai)
    
    individuoPai = valores[1][indicePai]
    individuoMae = valores[1][indiceMae]
    
    return individuoPai, individuoMae