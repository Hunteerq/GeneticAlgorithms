from libs.elite.best_strategy_base import BestStrategyBase


class EliteStrategy:

    def __init__(self, algorithm_configuration, number_of_best_chromosomes):
        self.__best_strategy_base = BestStrategyBase(algorithm_configuration, number_of_best_chromosomes)

    def get_best_chromosomes(self, population):
        return self.__best_strategy_base.get_best_chromosomes(population)
