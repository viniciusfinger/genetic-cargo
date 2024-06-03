from dashboard import open_dashboard
from genetic import *
from config import *
from web.grafic import *
from auxiliar import get_best_individual, generate_html_individual_items

#Cria a população inicial de forma psuedo-aleatória
population = create_population(individuals_number, items_number)

#Calcula o primeiro fitness da população 
fitness_history = [calculate_average_fitness(population, load_capacity, items)]

#Evolui, calcula e guarda o fitness da população até acabar as gerações
for generation in range(generations):
    population = evolve_population(population, load_capacity, items, individuals_number)
    fitness_average = calculate_average_fitness(population, load_capacity, items)
    fitness_history.append(fitness_average)

#Gera gráfico em PNG com histórico da média de fitness e valor total da carga do caminhão
generate_fitness_history_chart(fitness_history)

#Processa o melhor indivíduo, seu set de itens e processa e abre a página HTML 
best_individual = get_best_individual(population, items)
generate_html_individual_items(best_individual, items)

open_dashboard()
