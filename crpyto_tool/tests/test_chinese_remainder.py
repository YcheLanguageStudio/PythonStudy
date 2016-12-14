from crpyto_tool.libs.chinese_remainder_theorem import *

if __name__ == '__main__':
    remainder_solver = ChineseRemainder([37, 49])
    print remainder_solver.get_remainder_list(973)
    print remainder_solver.get_original_number(
        list_add(remainder_solver.get_remainder_list(678), remainder_solver.get_remainder_list(973)))
    print remainder_solver.get_original_number([23, 34])

    remainder_solver = ChineseRemainder([3, 5, 7])
    print remainder_solver.get_original_number([2, 3, 2])
