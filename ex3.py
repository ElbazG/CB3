import matplotlib.pyplot as plt
import numpy as np
import random

N = 10
nb_patterns = 10


def zero():
    with open('numbers_matrix/zero_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    return matrices


def one():
    with open('numbers_matrix/one_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    return matrices


def two():
    with open('numbers_matrix/two_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    return matrices


def three():
    with open('numbers_matrix/three_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    return matrices


def four():
    with open('numbers_matrix/four_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    return matrices


def five():
    with open('numbers_matrix/five_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    return matrices


def six():
    with open('numbers_matrix/six_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    return matrices


def seven():
    with open('numbers_matrix/seven_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    return matrices


def eight():
    with open('numbers_matrix/eight_matrix.txt') as matrices_file:
        matrices_buffer_list = matrices_file.buffer.read().decode().split("\r\n")
    a = [[int(ch) for ch in element] for element in [matrix for matrix in matrices_buffer_list]]
    matrices = np.array(a)
    return matrices


def nine():
    with open('numbers_matrix/nine_matrix.txt') as matrices_file:
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


def random_line(matrix):
    for i in matrix:
        num = random.randint(0, 9)
        if i[num] == 0:
            i[num] = 1
        else:
            i[num] = 0
    return matrix


def create():
    zero_matrix = zero()
    one_matrix = one()
    two_matrix = two()
    three_matrix = three()
    four_matrix = four()
    five_matrix = five()
    six_matrix = six()
    seven_matrix = seven()
    eight_matrix = eight()
    nine_matrix = nine()
    arr = [zero_matrix[0], one_matrix[0], two_matrix[0], three_matrix[0], four_matrix[0], five_matrix[0]
        , six_matrix[0], seven_matrix[0], eight_matrix[0], nine_matrix[0]]
    arr = np.array(arr)
    return arr


def train_network(matrix_array):
    # Train the network
    W = np.zeros((N * N, N * N))

    for i in range(N * N):
        for j in range(N * N):
            if i == j or W[i, j] != 0.0:
                continue

            w = 0.0

            for n in range(nb_patterns):
                w += matrix_array[n, i] * matrix_array[n, j]

            W[i, j] = w / matrix_array.shape[0]
            W[j, i] = W[i, j]
    return W


if __name__ == '__main__':
    only_one = create()
    weight = train_network(only_one)
    print(weight)