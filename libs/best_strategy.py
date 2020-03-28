from libs.best_strategy_base import BestStrategyBase


class BestStrategy:

    def __init__(self, algorithm_configuration, best_percentage):
        number_of_best_chromosomes = int(algorithm_configuration.population_number * best_percentage / 100)
        self.__best_strategy_base = BestStrategyBase(algorithm_configuration, number_of_best_chromosomes)

    def get_best_chromosomes(self, population):
        return self.__best_strategy_base.get_best_chromosomes(population)[0]
