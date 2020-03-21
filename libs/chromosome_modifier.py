import numpy as np


class ChromosomeModifier:

    def __init__(self, cross_prob, cross_homo_prob, mutation_prob, inversion_prob):
        self.__cross_prob = cross_prob
        self.__cross_homo_prob = cross_homo_prob
        self.__mutation_prob = mutation_prob
        self.__inversion_prob = inversion_prob

    def cross_one_point(self, tab_a, tab_b):
        if np.random.random() < self.__cross_prob:
            return self.__cross(tab_a, tab_b)
        else:
            return tab_a, tab_b

    def cross_two_point(self, tab_a, tab_b):
        if np.random.random() < self.__cross_prob:
            firs_cross_point = np.random.randint(len(tab_a)+1)
            tab_a[0:firs_cross_point], tab_b[0:firs_cross_point] = \
                self.__cross(tab_a[0:firs_cross_point], tab_b[0:firs_cross_point])
            tab_a[firs_cross_point:len(tab_a)], tab_b[firs_cross_point:len(tab_b)] = \
                self.__swap(tab_a[firs_cross_point:len(tab_a)], tab_b[firs_cross_point:len(tab_b)])
        return tab_a, tab_b

    def cross_three_point(self, tab_a, tab_b):
        if np.random.random() < self.__cross_prob:
            main_cross_point = np.random.randint(len(tab_a) + 1)
            tab_a[0:main_cross_point], tab_b[0:main_cross_point] = \
                self.__cross(tab_a[0:main_cross_point], tab_b[0:main_cross_point])
            tab_a[main_cross_point:len(tab_a)], tab_b[main_cross_point:len(tab_b)] = \
                self.__cross(tab_a[main_cross_point:len(tab_a)], tab_b[main_cross_point:len(tab_b)])
        return tab_a, tab_b

    def cross_homogeneous(self, tab_a, tab_b):
        if np.random.random() < self.__cross_prob:
            return self.__homogeneous_cross(tab_a, tab_b)
        return tab_a, tab_b

    def __homogeneous_cross(self, tab_a, tab_b):
        for index in range(0, len(tab_a)):
            if np.random.random() < self.__cross_homo_prob:
                tab_a[index], tab_b[index] = self.__swap(tab_a[index], tab_b[index])
        return tab_a, tab_b

    def __cross(self, tab_a, tab_b):
        cross_point = np.random.randint(len(tab_a) + 1)
        tab_a[0:cross_point], tab_b[0:cross_point] = self.__swap(tab_a[0:cross_point], tab_b[0:cross_point])
        return tab_a, tab_b

    def __swap(self, tab_a, tab_b):
        temp = np.copy(tab_a)
        tab_a = tab_b
        tab_b = temp
        return tab_a, tab_b

    def mutation_one_point(self, tab):
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




