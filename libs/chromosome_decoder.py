import numpy as np


class ChromosomeDecoder:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration

    def decode_chromosome(self, chromosome):
        chromosome_to_decode = np.array(chromosome)
        reversed_bit_integer_values = 2 ** np.arange(chromosome_to_decode.shape[0])
        bit_integer_values = reversed_bit_integer_values[::-1]

        return self.__algorithm_configuration.left_range_number \
               + (chromosome_to_decode.dot(bit_integer_values)) * self.__algorithm_configuration.range_dx
