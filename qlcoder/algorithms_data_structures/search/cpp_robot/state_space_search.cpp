#include <sstream>
#include "state_space_search.h"

int RobotSolver::GetConnectedCount(RobotMapType copy_map_arr) {
    auto bfs_mark_num = 0;
    auto row_num = copy_map_arr.size();
    auto col_num = copy_map_arr[0].size();
    auto start_row_idx = -1;
    auto start_col_idx = -1;

    for (auto row_idx = 0; row_idx < row_num; row_idx++) {
        bool is_break = false;
        for (auto col_idx = 0; col_idx < col_num; col_idx++) {
            if (copy_map_arr[row_idx][col_idx] == EMPTY_CHAR) {
                start_row_idx = row_idx;
                start_col_idx = col_idx;
                is_break = true;
                break;
            }
        }
        if (is_break) {
            break;
        }
    }

    queue<pair<int, int>> frontier_queue;
    frontier_queue.push(make_pair(start_row_idx, start_col_idx));
    copy_map_arr[start_row_idx][start_col_idx] = MARK_CHAR;

    for (; frontier_queue.size() > 0;) {
        //mark
        start_row_idx = frontier_queue.front().first;
        start_col_idx = frontier_queue.front().second;
        frontier_queue.pop();
        bfs_mark_num++;

        //expand
        if (start_row_idx - 1 >= 0 && copy_map_arr[start_row_idx - 1][start_col_idx] == EMPTY_CHAR) {
            frontier_queue.push(make_pair(start_row_idx - 1, start_col_idx));
            copy_map_arr[start_row_idx - 1][start_col_idx] = MARK_CHAR;
        }
        if (start_row_idx + 1 < row_num && copy_map_arr[start_row_idx + 1][start_col_idx] == EMPTY_CHAR) {
            frontier_queue.push(make_pair(start_row_idx + 1, start_col_idx));
            copy_map_arr[start_row_idx + 1][start_col_idx] = MARK_CHAR;
        }
        if (start_col_idx - 1 >= 0 and copy_map_arr[start_row_idx][start_col_idx - 1] == EMPTY_CHAR) {
            frontier_queue.push(make_pair(start_row_idx, start_col_idx - 1));
            copy_map_arr[start_row_idx][start_col_idx - 1] = MARK_CHAR;
        }
        if (start_col_idx + 1 < col_num and copy_map_arr[start_row_idx][start_col_idx + 1] == EMPTY_CHAR) {
            frontier_queue.push(make_pair(start_row_idx, start_col_idx + 1));
            copy_map_arr[start_row_idx][start_col_idx + 1] = MARK_CHAR;
        }
    }

    return bfs_mark_num;
}

bool RobotSolver::DepthFirstSearch(int init_row_idx, int init_col_idx, int marked_num,
                                   list<char> &path_list, RobotMapType &my_map_arr) {
    auto my_changed_row_idx = init_row_idx;
    auto my_changed_col_idx = init_col_idx;
    auto max_row_idx = my_map_arr.size() - 1;
    auto max_col_idx = my_map_arr[0].size() - 1;
    auto whole_num = row_num_ * col_num_;
    if (marked_num == whole_num)
        return true;
    else {
        //prune if there are more than one connected components
        if (GetConnectedCount(my_map_arr) != whole_num - marked_num)
            return false;

        //move left
        if (init_col_idx - 1 >= 0 and my_map_arr[init_row_idx][init_col_idx - 1] == EMPTY_CHAR) {
            for (auto idx = init_col_idx - 1; idx >= 0; idx--) {
                if (my_map_arr[init_row_idx][idx] == OCCUPY_CHAR)
                    break;
                else {
                    my_map_arr[init_row_idx][idx] = OCCUPY_CHAR;
                    my_changed_col_idx = idx;
                    marked_num++;
                }
            }

            path_list.push_back('l');
            if (DepthFirstSearch(init_row_idx, my_changed_col_idx, marked_num, path_list, my_map_arr))
                return true;
            else {
                path_list.pop_back();
                for (auto i = my_changed_col_idx; i < init_col_idx; i++) {
                    my_map_arr[init_row_idx][i] = EMPTY_CHAR;
                    marked_num--;
                }
                my_changed_col_idx = init_col_idx;
            }
        }

        //move right
        if (init_col_idx + 1 <= max_col_idx and my_map_arr[init_row_idx][init_col_idx + 1] == EMPTY_CHAR) {
            for (auto idx = init_col_idx + 1; idx <= max_col_idx; idx++) {
                if (my_map_arr[init_row_idx][idx] == OCCUPY_CHAR)
                    break;
                else {
                    my_map_arr[init_row_idx][idx] = OCCUPY_CHAR;
                    my_changed_col_idx = idx;
                    marked_num++;
                }
            }

            path_list.push_back('r');
            if (DepthFirstSearch(init_row_idx, my_changed_col_idx, marked_num, path_list, my_map_arr))
                return true;
            else {
                path_list.pop_back();
                for (auto i = my_changed_col_idx; i > init_col_idx; i--) {
                    my_map_arr[init_row_idx][i] = EMPTY_CHAR;
                    marked_num--;
                }
            }
        }

        //move up
        if (init_row_idx - 1 >= 0 and my_map_arr[init_row_idx - 1][init_col_idx] == EMPTY_CHAR) {
            for (auto idx = init_row_idx - 1; idx >= 0; idx--) {
                if (my_map_arr[idx][init_col_idx] == OCCUPY_CHAR)
                    break;
                else {
                    my_map_arr[idx][init_col_idx] = OCCUPY_CHAR;
                    my_changed_row_idx = idx;
                    marked_num++;
                }
            }

            path_list.push_back('u');
            if (DepthFirstSearch(my_changed_row_idx, init_col_idx, marked_num, path_list, my_map_arr))
                return true;
            else {
                path_list.pop_back();
                for (auto i = my_changed_row_idx; i < init_row_idx; i++) {
                    my_map_arr[i][init_col_idx] = EMPTY_CHAR;
                    marked_num--;
                }
                my_changed_row_idx = init_row_idx;
            }

        }

        //move down
        if (init_row_idx + 1 <= max_row_idx and my_map_arr[init_row_idx + 1][init_col_idx] == EMPTY_CHAR) {
            for (auto idx = init_row_idx + 1; idx <= max_row_idx; idx++) {
                if (my_map_arr[idx][init_col_idx] == OCCUPY_CHAR)
                    break;
                else {
                    my_map_arr[idx][init_col_idx] = OCCUPY_CHAR;
                    my_changed_row_idx = idx;
                    marked_num++;
                }
            }

            path_list.push_back('d');
            if (DepthFirstSearch(my_changed_row_idx, init_col_idx, marked_num, path_list, my_map_arr))
                return true;
            else {
                path_list.pop_back();
                for (auto i = my_changed_row_idx; i > init_row_idx; i--) {
                    my_map_arr[i][init_col_idx] = EMPTY_CHAR;
                    marked_num--;
                }
            }
        }

        return false;
    }

}

string RobotSolver::GetAnswerUrl() {
    stringstream my_str_builder;
    for (auto tmp_row_idx = 0; tmp_row_idx < robot_map_.size(); tmp_row_idx++) {
        for (auto tmp_col_idx = 0; tmp_col_idx < robot_map_[0].size(); tmp_col_idx++) {
            if (robot_map_[tmp_row_idx][tmp_col_idx] == EMPTY_CHAR) {
                list<char> tmp_list;
                cout << "Search On " << "(" << tmp_row_idx << " ," << tmp_col_idx << ")" << endl;
                auto new_map_arr = robot_map_;
                new_map_arr[tmp_row_idx][tmp_col_idx] = OCCUPY_CHAR;
                if (DepthFirstSearch(tmp_row_idx, tmp_col_idx, init_marked_num_ + 1, tmp_list, new_map_arr)) {
                    cout << "find it" << endl;
                    my_str_builder.clear();
                    my_str_builder << "x=" << tmp_row_idx + 1 << "&y=" << tmp_col_idx + 1 << "&path=";
                    for (auto my_char:tmp_list)
                        my_str_builder << my_char;
                    return my_str_builder.str();
                }
            }
        }
    }
    return "Not find";
}
