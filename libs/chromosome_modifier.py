import numpy as np


class ChromosomeModifier:

    def __init__(self, inversion_probability):
        self.__inversion_probability = inversion_probability

    def inversion(self, tab):
        return list(map(lambda el: self.__inverse(el), tab))

    def __inverse(self, el):
        if np.random.random() < self.__inversion_probability:
            return not el
        else:
            return el

