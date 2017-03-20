import numpy as np


def global_alignment(seq0, seq1):
    def get_dp_table():
        dp_score_table = np.ndarray(shape=(len(seq0) + 1, len(seq1) + 1), dtype=int)
        dp_score_table.fill(0)
        for col_idx in range(dp_score_table.shape[1]):
            dp_score_table[0][col_idx] = (-1) * col_idx
        for row_idx in range(dp_score_table.shape[0]):
            dp_score_table[row_idx][0] = (-1) * row_idx

        min_size = min(len(seq0), len(seq1))

        def match_score(i, j):
            return 1 if seq0[i - 1] == seq1[j - 1] else -1

        def transition_computation(i, j):
            gap_penalty = -1
            diagonal_val = dp_score_table[i - 1][j - 1] + match_score(i, j)
            right_val = dp_score_table[i][j - 1] + gap_penalty
            down_val = dp_score_table[i - 1][j] + gap_penalty
            dp_score_table[i][j] = max(diagonal_val, right_val, down_val)

        for iter_num in xrange(1, min_size + 1):
            transition_computation(iter_num, iter_num)
            # move right
            for col_idx in xrange(iter_num + 1, dp_score_table.shape[1]):
                transition_computation(iter_num, col_idx)

            # move down
            for row_idx in xrange(iter_num + 1, dp_score_table.shape[0]):
                transition_computation(row_idx, iter_num)

        return dp_score_table

    def traceback(table):
        """
        :type table: np.ndarray
        """
        gap_penalty = -1
        def match_score(i, j):
            return 1 if seq0[i - 1] == seq1[j - 1] else -1

        def dfs_detail(row_idx, col_idx, level):
            blank_str = ''.join(["  "] * level)[:-1] + '|_' if level > 0 else 'root'
            print '%-50s' % (blank_str + str((row_idx, col_idx))), 'score at', str((row_idx, col_idx)), ':', \
                table[row_idx][col_idx]

            if row_idx != 0 and col_idx != 0:
                # diagonal
                if table[row_idx - 1][col_idx - 1] + match_score(row_idx, col_idx) == table[row_idx][col_idx]:
                    dfs_detail(row_idx - 1, col_idx - 1, level + 1)
                # down
                if table[row_idx - 1][col_idx] + gap_penalty == table[row_idx][col_idx]:
                    dfs_detail(row_idx - 1, col_idx, level + 1)
                # right
                if table[row_idx][col_idx - 1] + gap_penalty == table[row_idx][col_idx]:
                    dfs_detail(row_idx, col_idx - 1, level + 1)

        dfs_detail(table.shape[0] - 1, table.shape[1] - 1, 0)

    dp_score_table = get_dp_table()
    print 'global alignment table:\n', dp_score_table, '\n'
    traceback(dp_score_table)


if __name__ == '__main__':
    seq_str0 = 'GGTTGACTA'
    seq_str1 = 'TGTTACGG'
    global_alignment(seq0=seq_str1, seq1=seq_str0)
