import matplotlib.pyplot as plt
import numpy as np

N = 10
nb_patterns = 1


def zero():
    with open('numbers_matrix/zero_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    return matrices


def show_matrix(num_list):
    plt.imshow(num_list)
    plt.show()


def convert_to_matrix(matrix):
    new_matrix = matrix.reshape(N, N)
    return new_matrix


if __name__ == '__main__':
    zero_matrix = zero()
    test = convert_to_matrix(zero_matrix[0])
    show_matrix(test)
