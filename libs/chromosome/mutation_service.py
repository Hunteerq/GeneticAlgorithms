import numpy as np

from libs.chromosome.chromosome_modifier import ChromosomeModifier
from libs.chromosome.mutation_types import MutationTypes


class MutationService:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__chromosome_modifier = ChromosomeModifier(algorithm_configuration.chromosome_config,
                                                        algorithm_configuration.left_range_number,
                                                        algorithm_configuration.right_range_number)

    def handle_mut(self, pop_to_mut):
        return [self.__apply_mut(chromosome) for chromosome in pop_to_mut]

    def __apply_mut(self, chromosome):
        mut_type = self.__algorithm_configuration.chromosome_config.mut_type

        if mut_type == MutationTypes.INDICES_SWAP.name:
            return self.__chromosome_modifier.mutation_indices_swap(chromosome)
        if mut_type == MutationTypes.STEADY.name:
            return self.__chromosome_modifier.mutation_steady(chromosome)
