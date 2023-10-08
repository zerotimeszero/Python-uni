class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = []

    def input_matrix(self):
        self.matrix = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                element = int(input(f"Введите элемент матрицы [{i+1}][{j+1}]: "))
                row.append(element)
            self.matrix.append(row)

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))

    def column_sum(self, column_index):
        if column_index < 0 or column_index >= self.m:
            return 0
        column_sum = 0
        for i in range(self.n):
            column_sum += self.matrix[i][column_index-1]
        return column_sum


    def zero_count(self):
        count = 0
        for row in self.matrix:
            count += row.count(0)
        return count

    def set_diagonal(self, scalar):
        for i in range(min(self.n, self.m)):
            self.matrix[i][i] = scalar