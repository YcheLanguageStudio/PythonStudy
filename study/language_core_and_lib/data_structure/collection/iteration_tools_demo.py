from itertools import combinations, chain


def demo_combinations():
    print 'demo combinations'
    my_tuple = (1, 2, 3, 4, 5)
    for tmp_tuple in combinations(my_tuple, 2):
        print tmp_tuple


if __name__ == '__main__':
    demo_combinations()
