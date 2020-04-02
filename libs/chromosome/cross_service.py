import numpy as np

from libs.chromosome.chromosome_modifier import ChromosomeModifier
from random import randrange

from libs.chromosome.cross_types import CrossTypes


class CrossService:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__chromosome_modifier = ChromosomeModifier(self.__algorithm_configuration.chromosome_config)

    def handle_cross(self, pop_to_cross):
        pop_to_cross_len = len(pop_to_cross)
        number_of_missing_chromosomes = self.__algorithm_configuration.population_number - pop_to_cross_len
        missing_chromosomes = []

        while len(missing_chromosomes) <= number_of_missing_chromosomes:
            first_chromosome = pop_to_cross[randrange(pop_to_cross_len)]
            second_chromosome = pop_to_cross[randrange(pop_to_cross_len)]

            missing_chromosomes.append(self.__apply_cross(first_chromosome, second_chromosome))

        return np.array(missing_chromosomes[0:number_of_missing_chromosomes]) + pop_to_cross

    def __apply_cross(self, first_chromosome, second_chromosome):
        cross_type = self.__algorithm_configuration.chromosome_config.cross_type

        if cross_type is CrossTypes.ONE_POINT:
            return self.__chromosome_modifier.cross_one_point(first_chromosome, second_chromosome)

        if cross_type is CrossTypes.TWO_POINTS:
            return self.__chromosome_modifier.cross_two_point(first_chromosome, second_chromosome)

        if cross_type is CrossTypes.THREE_POINTS:
            return self.__chromosome_modifier.cross_three_point(first_chromosome, second_chromosome)

        if cross_type is CrossTypes.HOMO:
            return self.__chromosome_modifier.cross_homogeneous(first_chromosome, second_chromosome)
