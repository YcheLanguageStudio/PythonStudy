import numpy as np


def yche_matrix_pow(a, b):
    if b == 1:
        return a
    else:
        return np.dot(yche_matrix_pow(a, b / 2), yche_matrix_pow(a, (b + 1) / 2))


def fib(n):
    primitive_matrix = np.matrix([[1, 1], [1, 0]])
    if n < 2:
        return n
    else:
        return yche_matrix_pow(primitive_matrix, n - 1).item(0, 0)


if __name__ == '__main__':
    print [fib(i) for i in xrange(10)]
