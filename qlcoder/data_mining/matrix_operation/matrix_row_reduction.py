import numpy as np

my_matrix = [[1 for col in range(3)] for row in range(3)]
my_vec = [1 for col in range(3)]
my_vec = np.dot(my_vec, my_matrix)

print 'result:' + reduce(lambda x, y: str(x) + ',' + str(y), my_vec)
my_matrix[0] = map(lambda x: x / reduce(lambda x, y: x + y + 0.0, my_matrix[0]), my_matrix[0])
print 'matrix:' + str(my_matrix)

my_matrix1 = np.dot(my_matrix, my_matrix)

print my_matrix1[0][1]

print np.multiply(my_matrix, my_matrix)
