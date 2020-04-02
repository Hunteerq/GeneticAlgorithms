from libs.algorithm.genetic_algorithm import GeneticAlgorithm


class Genetic:

    def __init__(self, alg_config):
        self.__gen_alg = GeneticAlgorithm(alg_config)
        best_pop = self.__gen_alg.evolve()
        # TODO MJ
        #  Add plots and save all results to file
        