
class ChromosomeConfig:

    def __init__(self, cross_prob, mut_prob, inv_prob):
        self.__cross_prob = cross_prob
        self.__mut_prob = mut_prob
        self.__inv_prob = inv_prob

    @property
    def cross_prob(self):
        return self.__cross_prob

    @property
    def mut_prob(self):
        return self.__mut_prob

    @property
    def inv_prob(self):
        return self.__inv_prob
