class Matrix:
    def __init__(self, *rows):
        self._matrix = [*rows]
    
    def __getitem__(self, index):
        if isinstance(index, int):
            return self._matrix[index]
        elif isinstance(index, tuple):
            if isinstance(index[0], int):
                row_number = index[0]
                col_number = index[1]

                return self._matrix[row_number][col_number]
            elif index[0] == None:
                columns = []

                for row in self._matrix:
                    columns.append([row[index[1]]])

                return columns

m1 = Matrix(
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

print(m1[1, 2])
print(m1[1])
print(m1[None, 2])