import numpy as np

from libs.chromosome.chromosome_modifier import ChromosomeModifier


class InversionService:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__chromosome_modifier = ChromosomeModifier(self.__algorithm_configuration.chromosome_config)

    def handle_inv(self, pop_to_inv):
        return np.apply_along_axis(self.__chromosome_modifier.inversion(), 1, pop_to_inv)
