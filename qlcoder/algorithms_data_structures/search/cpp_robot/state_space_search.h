#include <list>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <sstream>
#include <atomic>

using namespace std;

constexpr char MARK_CHAR = '2';
constexpr char OCCUPY_CHAR = '1';
constexpr char EMPTY_CHAR = '0';

class RobotSolver {
public:
    using RobotMapType = vector<vector<char>>;

    RobotSolver(int row_num, int col_num, string map_zero_one_str) : row_num_(row_num), col_num_(col_num),
                                                                     init_marked_num_(0) {
        for (auto my_ch:map_zero_one_str) {
            if (my_ch == OCCUPY_CHAR)
                init_marked_num_++;
        }

        robot_map_.resize(row_num_);
        for (auto &col:robot_map_) {
            col.resize(col_num_);
        }
        for (auto row_idx = 0; row_idx < row_num_; row_idx++) {
            for (auto col_idx = 0; col_idx < col_num_; col_idx++) {
                robot_map_[row_idx][col_idx] = map_zero_one_str[row_idx * col_num_ + col_idx];
            }
        }

        cout << row_num_<<","<<col_num_<<endl;
    }

    string GetAnswerUrl();

private:
    int row_num_;
    int col_num_;
    int init_marked_num_;
    RobotMapType robot_map_;


    int GetConnectedCount(RobotMapType robot_map);

    bool DepthFirstSearch(int init_row_idx, int init_col_idx, int marked_num, list<char>& path_list,
                          RobotMapType &my_map_arr);

};
