import numpy as np


class ChromosomeModifier:

    def __init__(self, inversion_prob, cross_prob):
        self.__inversion_prob = inversion_prob
        self.cross_prob = cross_prob

    def inversion(self, tab):
        return np.array(list(map(lambda el: self.__inverse(el), tab)))

    def __inverse(self, el):
        if np.random.random() < self.__inversion_prob:
            return np.int(not el)
        else:
            return np.int(el)

