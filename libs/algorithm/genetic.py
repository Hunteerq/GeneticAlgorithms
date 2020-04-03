from libs.algorithm.genetic_algorithm import GeneticAlgorithm


class Genetic:

    def __init__(self, alg_config):
        self.__gen_alg = GeneticAlgorithm(alg_config)
        solution_best_value, list_best, list_mean, list_std = self.__gen_alg.evolve()
        test = 1
        # TODO MJ
        #  Add plots and save all results to file
        