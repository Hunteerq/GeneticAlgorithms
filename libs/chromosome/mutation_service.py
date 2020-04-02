from libs.algorithm.function import Function
from libs.chromosome.mutation_types import MutationTypes


class MutationService:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__function = Function(self.__algorithm_configuration)

    def handle_mutation(self, population):
        return

