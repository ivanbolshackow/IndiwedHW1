class Matrix:
    def __init__(self, matrix_1, matrix_2):

        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def __str__(self, matrix=None):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

    def __add__(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.matrix_1)):

            for j in range(len(self.matrix_2[i])):
                matrix[i][j] = self.matrix_1[i][j] + self.matrix_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


my_matrix = Matrix([[10, 11, 9], [15, 11, 33], [5, 50, 6]],
                   [[25, 55, 32], [10, 3, 11], [5, 7, 45]])

print(my_matrix.__add__())
