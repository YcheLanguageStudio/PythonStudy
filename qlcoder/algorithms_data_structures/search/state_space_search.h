#include <list>
#include <string>
#include <vector>

using namespace std;

class RobotSolver {
private:
  int row_num_;
  int col_num_;
  RobotMapType robot_map_;

  RobotSolver(int row_num, int col_num, string map_zero_one_str)
      : row_num_(row_num), col_num_(col_num) {}

  bool DepthFirstSearch(int init_row, int init_col, int marked_num,
                        list<char> path_list, RobotMapType &rebot_map);

  int GetConnectedCount(RobotMapType robot_map);

public:
  using RobotMapType = vector<vector<unsigned char>>;
  string GetAnswerUrl();
};
