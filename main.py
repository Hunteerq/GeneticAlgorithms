from libs.chromosome_modifier import ChromosomeModifier
import numpy as np

if __name__ == '__main__':
    array_a = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    array_b = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(array_a)
    print(array_b)
    modifier = ChromosomeModifier(cross_prob=1.0,cross_homo_prob=0.2,
                                  mutation_prob=1.0, inversion_prob=1.0)
    array_a, array_b = modifier.cross_three_point(array_a, array_b)
    array_a = modifier.inversion(array_a)
    array_b = modifier.inversion(array_b)
    array_a = modifier.boundary_mutation_two_points(array_a)
    array_b = modifier.boundary_mutation_two_points(array_b)
    print(array_a)
    print(array_b)
