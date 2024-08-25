from random import getrandbits, random, randint
from typing import List
from Individual import Individual
from Item import Item

def create_individual(item_quantity: int) -> Individual:
    """
    Generate an array called chromossomes. Each position of this array (or one chromossome) 
    represents an item that will be taken in the truck if the value is 1, and 0 if it will 
    not be taken. Pseudo-random generated values by gentrandbits function for one bit 
    (can be 0 or 1).
    """
    chromossomes = [getrandbits(1) for _ in range(item_quantity)]
    return Individual(chromossomes)


def create_population(individuals_quantity: int, item_quantity: int) -> List[Individual]:
    return [create_individual(item_quantity) for _ in range(individuals_quantity)]


def calculate_average_fitness(population: List[Individual], max_weight: float, items: List[Item]):
    #todo: refactor this method above
    total_fitness = sum(calculate_fitness(individual, max_weight, items) for individual in population if calculate_fitness(individual, max_weight, items) >= 0)
    fitness_average = total_fitness / (len(population) * 1.0)
    
    return fitness_average

def calculate_fitness(individual: Individual, load_capacity: float, items: List[Item]) -> float:
    """
    Calculate the fitness of an individual. The fitness is the total value of the items that.
    """
    chromossomes = individual.get_chromossomes()
    total_weight = 0
    total_value = 0
    item_index = 0

    while item_index < len(chromossomes):
        total_weight = total_weight + (chromossomes[item_index] * items[item_index].getWeight())
        total_value = total_value + (chromossomes[item_index] * items[item_index].getPrice())
        item_index += 1

    if (load_capacity - total_weight) < 0:
        return -1 #Peso total do caminhão excedido. //todo: maybe trhow a exception.
    else:
        return total_value
    
def evolve_population(population: List[Individual], load_capacity: float, items: List[Item], indivibuals_number: int, mutation_rate=0.05):
    #Classifica o fitness e seu respectivo indivíduo em um array
    parents_individuals = [[calculate_fitness(individual, load_capacity, items), individual] for individual in population if calculate_fitness(individual,load_capacity, items) >= 0]
    
    # Order by fitness decreasing
    parents_individuals.sort(reverse=True, key=lambda x: x[0])
    
    #individuals reprodution
    children_individuals = []

    while len(children_individuals) < indivibuals_number:
        # todo: should return individuals objects instead list
        dad, mom = draw_parents(parents_individuals)
        half_chromossome_index = len(dad.get_chromossomes()) // 2

        #Filho vai ser a primeira metade do pai + a primeira metade da mãe
        children = dad.get_chromossomes()[:half_chromossome_index] + mom.get_chromossomes()[half_chromossome_index:]
        children_individuals.append(children)

    '''Há 5% de chance (definido no parâmetro "mutacao" do método)
    de fazer uma mutação em um cromossomo do indivíduo'''
    for children in children_individuals:
        if mutation_rate > random():
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
    item_quantity = len(individual.get_chromossomes())
    total_value = 0

    for i in range(item_quantity):
        if individual[i] == 1:
            total_value += items[i].getPrice()
        
    return total_value