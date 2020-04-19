import numpy as np


class ChromosomeModifier:

    def __init__(self, chromosome_config):
        self.__chromosome_config = chromosome_config

    def mutation_indices_swap(self, tab):
        if np.random.random() < self.__chromosome_config.mut_prob:
            tab[0], tab[1] = tab[1], tab[0]
            return tab
        return tab

    def cross_arithmetic(self, tab_a, tab_b):
        if np.random.random() < self.__chromosome_config.cross_prob:
            return self.__handle_cross_arithmetic(tab_a, tab_b)
        return tab_a, tab_b

    @staticmethod
    def __handle_cross_arithmetic(tab_a, tab_b):
        k = np.random.random()
        x1_new = k * tab_a[0] + (1 - k) * tab_b[0]
        y1_new = k * tab_a[1] + (1 - k) * tab_b[1]
        x2_new = (1 - k) * tab_a[0] + k * tab_b[0]
        y2_new = (1 - k) * tab_a[1] + k * tab_b[1]
        return np.array([x1_new, y1_new]), np.array([x2_new, y2_new])
