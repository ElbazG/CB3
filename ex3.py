import matplotlib.pyplot as plt
import numpy as np

N = 10
nb_patterns = 10


def zero():
    with open('numbers_matrix/zero_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    print(matrices[0])


def show_matrix(num_list):
    plt.imshow()


if __name__ == '__main__':
    zero()
    pass
    # first = zero()
    # print(first[0])
