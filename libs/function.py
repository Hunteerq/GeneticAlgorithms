import numpy as np

from chromosome_decoder import ChromosomeDecoder


class Function:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__chromosome_decoder = ChromosomeDecoder(self.__algorithm_configuration)

    @staticmethod
    def evaluate(input_variables):
        x1, x2 = input_variables

        return (1.5 - x1 + x1*x2)**2 + (2.25 - x1 + x1*x2**2)**2 + (2.625 - x1 + x1*x2**3)**2

    def evaluate_chromosome(self, chromosome):
        decoded_chromosome = self.__chromosome_decoder.decode_chromosome(chromosome)

        return self.evaluate(decoded_chromosome)

    def evaluate_population(self, population):
        return np.apply_along_axis(self.evaluate_chromosome, 1, population)

    def get_best_chromosome_for_epoch(self, population):
        evaluated_population = self.evaluate_population(population)
        index = np.argmax(evaluated_population)

        return population[index], evaluated_population[index]
