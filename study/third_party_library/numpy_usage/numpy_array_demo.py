import numpy as np


def demo_1d_arr():
    py_list = [i for i in range(6)]
    np_arr = np.asarray(py_list)
    print type(np_arr)
    print np_arr, np_arr.shape


def demo_matrix():
    col_num = 5
    row_num = 4
    py_list = [map(lambda ele: i * col_num + ele, [j for j in range(col_num)]) for i in range(row_num)]
    np_matrix = np.asarray(py_list)
    print type(np_matrix)
    print np_matrix


def demo_element_wise_op():
    np_arr = np.array([1, 2, 3])
    print np_arr
    np_arr -= 1
    print np_arr


if __name__ == '__main__':
    demo_1d_arr()
    demo_matrix()
    demo_element_wise_op()
