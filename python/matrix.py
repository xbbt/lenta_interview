# Напишите программу для базовой линейной алгебры без
# использования сторонних библиотек (напр. NumPy).
# Требуемые функции: сложение, вычитание, умножение, деление,
# транспонирование и определитель.

def minor(m, i, j):
    mo = m[:i] + m[i + 1:]
    return [k[:j] + k[j + 1:] for k in mo]


def det(m):
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        # print(m[0][0] * m[1][1] - m[0][1] * m[1][0])
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        res = 0
        for i in range(len(m)):
            # print(res)
            res += (-1) ** i * m[0][i] * det(minor(m, 0, i))
    return res


class Matrix(object):
    def __init__(self, values, columns, rows):
        self.values = []
        self.col_num = None
        self.row_num = None
        try:
            if isinstance(columns, int):
                if columns > 0:
                    self.col_num = columns
                else:
                    raise ValueError
            else:
                raise TypeError
        except (TypeError, ValueError) as er:
            print('The number of columns should be a positive integer number')
            raise er

        try:
            if isinstance(rows, int):
                if rows > 0:
                    self.row_num = rows
                else:
                    raise ValueError
            else:
                raise TypeError
        except (TypeError, ValueError) as er:
            print('The number of rows should be a positive integer number')
            raise er

        try:
            if (len(values) == self.col_num * self.row_num
               and all(isinstance(num, (int, float)) for num in values)):
                for i in range(self.row_num):
                    self.values.append(
                        tuple(values[i*self.col_num:(i+1)*self.col_num])
                    )
            else:
                raise ValueError
        except (TypeError, ValueError) as er:
            print('The values should be a collection of'
                  ' numbers with the length that is equal to'
                  ' product of the number of columns and'
                  ' the number of rows')
            raise er

    def __repr__(self):
        if self.values:
            res = ''
            for row in self.values:
                res += str(row)+'\n'
            return res[:-1]
        else:
            return 'Empty matrix'

    def transpose(self):
        new_values = []
        for i in zip(*self.values):
            new_values.extend(i)
        return Matrix(new_values, self.row_num, self.col_num)

    def __add__(self, other):
        try:
            if (self.col_num == other.col_num
               and self.row_num == other.row_num):
                result_values = []
                try:
                    for i, row in enumerate(self.values):
                        for j, value in enumerate(row):
                            result_values.append(value + other.values[i][j])
                    return Matrix(result_values, self.col_num, self.row_num)
                except TypeError:
                    print('Matrices are not summable.')
                    raise TypeError
            else:
                print("Matrices have different shapes.")
                raise ValueError
        except AttributeError:
            print("The second term doesn't have shape attributes.")

    def __sub__(self, other):
        try:
            if (self.col_num == other.col_num
               and self.row_num == other.row_num):
                result_values = []
                try:
                    for i, row in enumerate(self.values):
                        for j, value in enumerate(row):
                            result_values.append(value - other.values[i][j])
                    return Matrix(result_values, self.col_num, self.row_num)
                except TypeError:
                    print('Matrices are not subtractive.')
                    raise TypeError
            else:
                print("Matrices have different shapes.")
                raise ValueError
        except AttributeError:
            print("The subtrahend doesn't have shape attributes.")

    def __mul__(self, other):
        try:
            if self.col_num == other.row_num:
                result_values = []
                try:
                    for i in range(self.row_num):
                        for j in range(other.col_num):
                            res_ij = 0
                            for k in range(self.col_num):
                                res_ij += self.values[i][k] * other.values[k][j]
                            result_values.append(res_ij)
                    return Matrix(result_values, self.row_num, other.col_num)
                except TypeError:
                    print('Matrices are not subtractive.')
                    raise TypeError
            else:
                print("Matrices have wrong shapes.")
                raise ValueError
        except AttributeError:
            print("The multiplier doesn't have shape attributes.")

    def det(self):
        if self.col_num == self.row_num:
            return det(self.values)
        else:
            print('The matrix is not square. The determinant is not defined')
            raise ValueError

    def inverse(self):
        if self.col_num == self.row_num:
            determinant = det(self.values)
            adj_values = []
            if determinant != 0:
                for i in range(self.col_num):
                    for j in range(self.row_num):
                        adj_values.append(
                            (-1)**(i+j)*det(minor(self.values, i, j)) / determinant
                        )
                res = Matrix(adj_values, columns=self.col_num, rows=self.row_num)
                return res.transpose()
            else:
                print('Sorry, but this matrix has too small rank'
                      ' to have an inverse.')
        else:
            print("The matrix is not square. It does not have an inverse.")
            raise ValueError

    def __truediv__(self, other):
        if self.col_num == self.row_num == other.col_num == other.row_num:
            return self * other.inverse()
        else:
            print('Matrices are not square, or have different shapes.')
            raise ValueError


if __name__ == '__main__':
    a = Matrix(
        values=[1, 2, 3, 4, 5, 6],
        columns=2, rows=3
    )
    print('Matrix A\n', a, 'and its transposed version\n',  a.transpose())

    print('A + A\n', a + a)

    b = Matrix(
        values=[1, 2, 3, 4],
        columns=2, rows=2
    )
    print('Matrix B\n', b)
    print('Matrix B * B')
    print(b*b)
    bb = b*b
    print('Determinant of B = ', b.det(), '. Determinant of B*B = ', bb.det())

    print('B / B \n', b / b)

    e = Matrix(
        values=[
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ],
        columns=4, rows=4
    )
    print('Identity_matrix\n', e, 'and its determinant = ', e.det())
