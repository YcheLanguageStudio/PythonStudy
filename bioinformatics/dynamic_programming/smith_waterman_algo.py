import numpy as np


def global_alignment(seq0, seq1):
    def get_dp_table():
        dp_score_table = np.ndarray(shape=(len(seq0) + 1, len(seq1) + 1), dtype=int)
        dp_score_table.fill(0)
        print dp_score_table
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

    print get_dp_table()


if __name__ == '__main__':
    seq_str0 = 'GGTTGACTA'
    seq_str1 = 'TGTTACGG'
    global_alignment(seq0=seq_str0, seq1=seq_str1)
