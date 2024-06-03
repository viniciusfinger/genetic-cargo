from random import getrandbits, random, randint

def create_individual(numeroDeItens):
    """
    Gera um array chamado indivíduo (cromossomos), onde cada posição desse array 
    representa um item que caso estiver com 1 no valor será levado no caminhão 
    e 0 não será levado.
    """
    individual = [getrandbits(1) for x in range(numeroDeItens)]
    return individual

def create_population(numeroDeIndividuos, numeroDeItens):
    #Cria a populacao de individuos
    population = [create_individual(numeroDeItens) for x in range(numeroDeIndividuos)]
    return population

def calculate_average_fitness(population, pesoMaximo, itens):
    #Calcula a avaliação media da população de indivíduos
    total_fitness = sum(calculate_fitness(individual, pesoMaximo, itens) for individual in population if calculate_fitness(individual, pesoMaximo, itens) >= 0)
    fitness_average = total_fitness / (len(population) * 1.0)
    
    return fitness_average

def calculate_fitness(individual, load_capacity, items):
    #Faz a avaliação de um único indivíduo
    total_weight = 0
    total_value = 0
    item_index = 0

    while item_index < len(individual):
        total_weight = total_weight + (individual[item_index] * items[item_index].getPeso())
        total_value = total_value + (individual[item_index] * items[item_index].getValor())
        item_index += 1

    if (load_capacity - total_weight) < 0:
        return -1 #Peso total do caminhão excedido.
    else:
        return total_value
    
def evolve_population(population, load_capacity, items, indivibuals_number, mutation=0.05):
    #Classifica o fitness e seu respectivo indivíduo em um array
    parents_individuals = [[calculate_fitness(individual, load_capacity, items), individual] for individual in population if calculate_fitness(individual,load_capacity, items) >= 0]
    parents_individuals.sort(reverse=True)

    #Reprodução dos indivíduos
    children_individuals = []

    while len(children_individuals) < indivibuals_number:
        dad, mom = draw_parents(parents_individuals)
        half_chromossome_index = len(dad) // 2

        #Filho vai ser a primeira metade do pai + a primeira metade da mãe
        children = dad[:half_chromossome_index] + mom[half_chromossome_index:]
        children_individuals.append(children)

    '''Há 5% de chance (definido no parâmetro "mutacao" do método)
    de fazer uma mutação em um cromossomo do indivíduo'''
    for children in children_individuals:
        if mutation > random():
            chromossome_to_change = randint(0, len(children)-1)
            
            #to-do: estudar uma maneira mais bonita de fazer isso
            if children[chromossome_to_change] == 1:
                children[chromossome_to_change] = 0
            else:
                children[chromossome_to_change] = 1
    
    return children_individuals

def draw_parents(parents_individuals):
    #Sorteia um pai e uma mãe baseado na regra da roleta

    def draw_index(total_fitness, ignored_index =-1):
        #Indice ignorado = indice do pai, para não ser sorteado de novo.

        roulette = []
        accumulated = 0
        
        drawn_value = random()

        #fitness total ignora o indivíduo pai, se já houver
        if ignored_index != -1:
            total_fitness -= values[0][ignored_index]        
        
        for index, i in enumerate(values[0]):
            if ignored_index == index:
                continue
            accumulated += i
            roulette.append(accumulated/total_fitness)

            if roulette[-1] >= drawn_value:
                return index
    
    #Cria duas listas com os valores de fitness e indivíduos
    values = list(zip(*parents_individuals))
    total_fitness = sum(values[0])

    dad_index = draw_index(total_fitness)
    mom_index = draw_index(total_fitness, dad_index)
    
    dad_individual = values[1][dad_index]
    mom_individual = values[1][mom_index]
    
    return dad_individual, mom_individual