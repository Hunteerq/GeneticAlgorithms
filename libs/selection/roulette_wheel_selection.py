import numpy as np


class RouletteWheelSelection:

    def __init__(self, function, is_max_opt):
        self.__function = function
        self.__is_max_opt = is_max_opt

    def get_population(self, old_pop):
        old_pop = np.sort(old_pop)
        eval_pop = self.__function.evaluate_population(old_pop)
        if not self.__is_max_opt:
            eval_pop = 1/eval_pop
        corrected_eval_pop = eval_pop + abs(eval_pop.min())
        wheel = np.cumsum(corrected_eval_pop)
        new_pop = []
        for el in np.random.rand(np.shape(old_pop)[0]):
            new_pop.append(old_pop[(wheel > el * wheel.max())][0])
        return np.array(new_pop)

