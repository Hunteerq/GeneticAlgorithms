import numpy as np

from libs.chromosome.chromosome_modifier import ChromosomeModifier
from libs.chromosome.mutation_types import MutationTypes


class MutationService:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__chromosome_modifier = ChromosomeModifier(self.__algorithm_configuration.chromosome_config)

    def handle_mut(self, pop_to_cross):
        return np.apply_along_axis(self.__apply_mut(), 1, pop_to_cross)

    def __apply_mut(self, chromosome):
        mut_type = self.__algorithm_configuration.chromosome_config.mut_type

        if mut_type is MutationTypes.ONE_POINT:
            return self.__chromosome_modifier.boundary_mutation_one_point(chromosome)

        if mut_type is MutationTypes.TWO_POINTS:
            return self.__chromosome_modifier.boundary_mutation_two_points(chromosome)
