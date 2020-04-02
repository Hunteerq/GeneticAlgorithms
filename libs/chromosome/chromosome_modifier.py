import numpy as np


class ChromosomeModifier:

    def __init__(self, cross_prob, mutation_prob, inversion_prob):
        self.__cross_prob = cross_prob
        self.__mutation_prob = mutation_prob
        self.__inversion_prob = inversion_prob

    def mutation(self, tab):
        return np.array([self.__mutate(el) for el in tab])

    def __mutate(self, el):
        if np.random.random() < self.__mutation_prob:
            return np.int(not el)
        else:
            return np.int(el)

    def inversion(self, tab):
        if np.random.random() < self.__inversion_prob:
            return self.__invert(tab)
        else:
            return tab

    def __invert(self, tab):
        start = np.random.randint(0, len(tab))
        end = np.random.randint(start, len(tab))
        tab[start:end] = np.flip(tab[start:end])
        return tab


