def min_sum(weight_matrix):
    unmark_flag = 0
    mark_flag = 1
    row_num = len(weight_matrix)
    col_num = len(weight_matrix[0])
    min_sum_matrix = [[0 for _ in range(col_num)] for _ in range(row_num)]
    mark_matrix = [[0 for _ in range(col_num)] for _ in range(row_num)]
    prev_pos_matrix = [[None for _ in range(col_num)] for _ in range(row_num)]

    def min_sum_detail(i, j):
        if mark_matrix[i][j] == unmark_flag:
            if i == 0 and j == 0:
                min_sum_matrix[i][j] = weight_matrix[0][0]
            elif i == 0:
                min_sum_matrix[i][j] = min_sum_detail(0, j - 1) + weight_matrix[0][j]
                prev_pos_matrix[i][j] = [(0, j - 1)]
            elif j == 0:
                min_sum_matrix[i][j] = min_sum_detail(i - 1, 0) + weight_matrix[i][0]
                prev_pos_matrix[i][j] = [(i - 1, 0)]
            else:
                min_sum_matrix[i][j] = min(min_sum_detail(i, j - 1) + weight_matrix[i][j],
                                           min_sum_detail(i - 1, j) + weight_matrix[i][j])
                prev_pos_matrix[i][j] = []
                if min_sum_detail(i, j - 1) + weight_matrix[i][j] == min_sum_matrix[i][j]:
                    prev_pos_matrix[i][j].append((i, j - 1))
                if min_sum_detail(i - 1, j) + weight_matrix[i][j] == min_sum_matrix[i][j]:
                    prev_pos_matrix[i][j].append((i - 1, j))

            mark_matrix[i][j] = mark_flag

        return min_sum_matrix[i][j]

    def print_tree():
        def dfs_detail(node_ref, node_level):
            blank_str = ''.join(["  "] * node_level)[:-1] + '|_' if node_level > 0 else 'root'
            print '%-50s' % (blank_str + str(node_ref))
            if node_ref is None:
                return
            else:
                for i, j in node_ref:
                    dfs_detail(prev_pos_matrix[i][j], node_level + 1)

        dfs_detail([(row_num - 1, col_num - 1)], 0)

    print prev_pos_matrix
    min_sum_val = min_sum_detail(row_num - 1, col_num - 1)
    print_tree()
    return min_sum_val


if __name__ == '__main__':
    matrix = [[1, 2, 9], [3, 4, 8], [5, 6, 7]]
    print min_sum(matrix)
