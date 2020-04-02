from libs.algorithm.function import Function
from libs.elite.best_strategy import BestStrategy
from libs.selection.roulette_wheel_selection import RouletteWheelSelection
from libs.selection.selection_types import SelectionTypes
from libs.selection.tournament_selection import TournamentSelection


class SelectionService:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__best_strategy = BestStrategy(self.__algorithm_configuration, 10)
        self.__function = Function(self.__algorithm_configuration)
        self.__roulette_wheel_selection = RouletteWheelSelection(self.__function)
        self.__tournament_selection = TournamentSelection(self.__algorithm_configuration, 3)

    def handle_selection(self, population):
        new_population = self.__algorithm_configuration.selection_method = {
            SelectionTypes.BEST: self.__best_strategy.get_best_chromosomes(population),
            SelectionTypes.ROULETTE: self.__roulette_wheel_selection(population),
            SelectionTypes.TOURNAMENT: self.__tournament_selection(population)
        }

        return new_population

