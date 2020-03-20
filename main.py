from libs.chromosome_modifier import ChromosomeModifier
import numpy as np

if __name__ == '__main__':
    array = np.array([1, 0, 0, 0, 1, 1, 0, 1])
    print(array)
    mod = ChromosomeModifier(0.2, 0.3)
    print(mod.inversion(array))
    print(type(mod.inversion(array)))


