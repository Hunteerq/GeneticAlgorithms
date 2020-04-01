import numpy as np


class RouletteWheelSelection:

    def __init__(self, ret_pop_amount, function):
        self.__ret_pop_amount = ret_pop_amount
        self.__function = function

    def get_population(self, old_pop):
        old_pop = np.sort(old_pop)
        eval_pop = self.__function.evaluate_population(old_pop)
        corrected_eval_pop = eval_pop + abs(eval_pop.min()) + 1
        wheel = np.cumsum(corrected_eval_pop)
        new_pop = []
        for el in np.random.rand(np.shape(old_pop)[0]):
            new_pop.append(old_pop[(wheel > el * wheel.max())][0])
        return np.array(new_pop)

