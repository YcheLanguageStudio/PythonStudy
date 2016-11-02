import json


def get_piece_list(pieces_info):
    return [transform_piece_str_to_grid(ele) for ele in pieces_info]


def transform_piece_str_to_grid(piece_str):
    rows = piece_str.split(',')
    return [map(lambda info_ch: 1 if info_ch == 'X' else 0, row) for row in rows]


def transform_map_str_to_grid(map_str):
    return [map(lambda info_ch: ord(info_ch) - ord('0'), row) for row in map_str]


def sum_piece_arr(piece_arr):
    my_sum = 0
    for row in piece_arr:
        for col in row:
            my_sum += col
    return my_sum


my_dict = {"level": 29, "modu": "3", "map": ["202220", "202112", "220000", "200201", "211221", "212001", "021211"],
           "pieces": ["XXXXX,XXXX.,XX...", "..X.,.XX.,XXXX,X...", "...X,..XX,.XX.,XX..", ".X..,.XX.,XXX.,XXXX,.X..",
                      "XXX,..X,.XX", "XXX,.XX,..X", "X...,XXXX,XX..,.X..,.X..", "...X,..XX,.XXX,..X.,XXX.",
                      ".X...,.X...,.XX..,XXXXX", ".X..,XXXX,.XX.,..XX,...X", ".X.,.XX,.X.,XX.,XX.", "X.,XX,.X,.X",
                      ".X.,.XX,.X.,XX.,XXX"]}
before_pieces_info = get_piece_list(pieces_info=my_dict['pieces'])

print before_pieces_info
extended_tuple_info = [(before_pieces_info[i], i, sum_piece_arr(before_pieces_info[i])) for i in
                       range(0, len(before_pieces_info))]
print extended_tuple_info
extended_tuple_info.sort(lambda left, right: right[2] - left[2])

print extended_tuple_info
before_sol_str = '11210122003101221000313333'
two_pos_list = list()

for i in range(0, len(before_sol_str) / 2):
    two_pos_list.append(before_sol_str[2 * i] + before_sol_str[2 * i + 1])

print two_pos_list
tmp_list = ['' for i in range(0, len(before_sol_str) / 2)]

for idx in range(0, len(before_sol_str)/2):
    print extended_tuple_info[idx][1]
    tmp_list[extended_tuple_info[idx][1]] = two_pos_list[idx]

print ''.join(tmp_list)
