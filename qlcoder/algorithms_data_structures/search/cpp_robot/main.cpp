#include <iostream>
#include "state_space_search.h"

using namespace std;

int main(int argc, char *argv[]) {
    int my_row_num_int = stoi(argv[1]);
    int my_col_num_int = stoi(argv[2]);
    string my_map_str = argv[3];

    RobotSolver robotSolver(my_row_num_int, my_col_num_int, my_map_str);
    cout << robotSolver.GetAnswerUrl() << endl;
    return 0;

}