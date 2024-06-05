from genetic import *
from config import *

population = create_population(individuals_number, items_number)

fitness_history = []
fitness_history.append(calculate_average_fitness(population, load_capacity, items))

for generation in range(generations):
    population = evolve_population(population, load_capacity, items, individuals_number)
    fitness_average = calculate_average_fitness(population, load_capacity, items)
    fitness_history.append(fitness_average)
