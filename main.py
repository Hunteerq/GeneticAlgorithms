import sys

from PyQt5.QtWidgets import QApplication

from libs.algorithm_configuration_provider import AlgorithmConfigurationProvider
from libs.chromosome_modifier import ChromosomeModifier
import numpy as np

from libs.function import Function
from libs.main import Main
from libs.population_generator import PopulationGenerator
from libs.roulette_wheel_selection import RouletteWheelSelection

if __name__ == '__main__':
    # algorithm_configuration = AlgorithmConfigurationProvider(2, 3, 4, 4, 10, True)
    # function = Function(algorithm_configuration)
    # roulette = RouletteWheelSelection(2, function)
    # population_generator = PopulationGenerator(algorithm_configuration)
    # population = population_generator.generate_population()
    #
    # res = roulette.get_population(population)
    # print(res)
    # print(array_a)
    # print(array_b)
    # modifier = ChromosomeModifier(cross_prob=1.0, cross_homo_prob=0.2,
    #                               mutation_prob=1.0, inversion_prob=1.0)
    # array_a, array_b = modifier.cross_three_point(array_a, array_b)
    # array_a = modifier.inversion(array_a)
    # array_b = modifier.inversion(array_b)
    # array_a = modifier.boundary_mutation_two_points(array_a)
    # array_b = modifier.boundary_mutation_two_points(array_b)
    # print(array_a)
    # print(array_b)
    app = QApplication(sys.argv)
    window = Main()
    app.exec_()
