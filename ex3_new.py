import numpy as np
from matplotlib import pyplot as plt

value = -1


# Print the matrix image
def show_matrix(matrix):
    plt.imshow(matrix)
    plt.show()


# Train neural network
def train_network(matrix):
    values = []
    for i in range(100):
        line = []
        for j in range(100):
            grade = 0
            for k in range(10):
                if matrix[k][i] == matrix[k][j]:
                    grade += 1
                else:
                    grade -= 1
            line.append(grade)
        values.append(line)
    return np.array(values)


# Try to recover the learned pattern
def recover(matrix, t_mat):
    original_matrix = np.copy(matrix)
    worked_matrix = np.copy(matrix)
    h_vector = np.arange(100)
    np.random.shuffle(h_vector)
    sign = True

    while sign:
        sign = False
        for sample in range(100):
            sum = 0
            for i in range(100):
                if i != h_vector[sample]:
                    sum = sum + (worked_matrix[i] * t_mat[h_vector[sample]][i])
            recovery = worked_matrix[h_vector[sample]]
            if sum >= 0:
                worked_matrix[h_vector[sample]] = 1
            else:
                worked_matrix[h_vector[sample]] = value
            if recovery != worked_matrix[h_vector[sample]]:
                sign = True
    show_matrix(original_matrix.reshape(10, 10))
    show_matrix(worked_matrix.reshape(10, 10))
    return worked_matrix


# Randomize the data
def randomize(matrix, rate):
    matrix_list = []
    for _ in range(10):
        index_array = np.arange(matrix.size)
        np.random.shuffle(index_array)
        index_array = index_array[:rate]

        mutated_matrix = np.copy(matrix)
        for m in range(rate):
            if mutated_matrix[index_array[m]] == 1:
                mutated_matrix[index_array[m]] = value
            else:
                mutated_matrix[index_array[m]] = 1
        matrix_list.append(mutated_matrix)
    return matrix_list


# Read the input file
with open("numbers.txt", 'r') as data_file:
    data = []
    holder = []
    for line in data_file:
        if line.rstrip() == "":
            holder = np.array(holder)
            holder = np.where(holder == 0, value, holder)
            data.append(holder)
            holder = []
        else:
            holder.append([int(bit) for bit in line.rstrip()])
    holder = np.array(holder)
    holder = np.where(holder == 0, value, holder)
    data.append(holder)

# Create matrix data-base
data_base = []
matrix_data = []
for d in data:
    matrix_data.append(d.reshape(100))
    if len(matrix_data) == 10:
        data_base.append(np.array(matrix_data))
        matrix_data = []

trained_matrix = []
for m in data_base:
    trained_matrix.append(train_network(m))

# Core of the code - try to reconstruct
scores = []
for rate in range(5, 51, 5):
    mutated_data = randomize(data[0].reshape(100), rate)
    nums_scores = []
    for num_lern in range(1, 11, 1):
        t_of_all = np.zeros((100, 100))
        for i in range(num_lern):
            t_of_all = t_of_all + trained_matrix[i]
        t_of_all = t_of_all / (num_lern + 1)

        sum_n_avg = 0
        for i in range(10):
            recon_matrix = recover(mutated_data[i], t_of_all)
            sum_n_avg = sum_n_avg + np.linalg.norm(data[0].reshape(100) - recon_matrix)
            sum_n_avg = sum_n_avg / 10
        nums_scores.append(sum_n_avg)
    scores.append(nums_scores)

"""
# Plotting using matplob lib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = ['olive', 'yellow', 'olivedrab', 'yellowgreen', 'darkolivegreen', 'greenyellow',
          'chartreuse', 'lawngreen', 'darkseagreen', 'palegreen']
markers = ['8', 's', 'p', 'P', '*', "+", "X", "D", "x", "|"]

for i in range(len(colors)):
    ax.scatter(0, 0, 0, color=colors[i], marker='.', label=i + 1)

for i in range(len(markers)):
    ax.scatter(0, 0, 0, color='k', marker=markers[i], label=(i + 1) * 5)

for ratio in range(len(scores)):
    for number in range(len(scores[ratio])):
        ax.scatter(number, (ratio + 1) * 10, scores[ratio][number], color=colors[number], marker=markers[ratio])

ax.set_xlabel('Number')
ax.set_ylabel('Change Rate')
ax.set_zlabel('Difference')
plt.legend(bbox_to_anchor=(1.5, 1), loc='best')
plt.show()
"""