import numpy as np
from algorithm_configuration_provider import AlgorithmConfigurationProvider
from elite_strategy import EliteStrategy
from population_generator import PopulationGenerator
from chromosome_decoder import ChromosomeDecoder
from function import Function
from tournament_selection import TournamentSelection

algorithm_configuration = AlgorithmConfigurationProvider(2, 3, 3, 4, 1)
population_generator = PopulationGenerator(algorithm_configuration)
population = population_generator.generate_population()
print(population)
chromosome_decoder = ChromosomeDecoder(algorithm_configuration)
#
#print(chromosome_decoder.decode_chromosome(population[0]))
#print(chromosome_decoder.decode_chromosome(population[1]))
#print(chromosome_decoder.decode_chromosome(population[2]))

function = Function(algorithm_configuration)
#print(function.evaluate_population(population))

elite_strategy = EliteStrategy(algorithm_configuration, 2)
#print(elite_strategy.get_best_chromosomes(population))

tournament_selection = TournamentSelection(algorithm_configuration, 2)
print(tournament_selection.handle_selection(population))
