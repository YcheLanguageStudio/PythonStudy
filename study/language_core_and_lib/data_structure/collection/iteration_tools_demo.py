from itertools import combinations, chain


def demo_combinations():
    print 'demo combinations'
    my_tuple = (1, 2, 3, 4, 5)
    for tmp_tuple in combinations(my_tuple, 2):
        print tmp_tuple


def demo_enumeration():
    my_list = [1, 2, 3, 4, 5]
    for idx, val in enumerate(my_list):
        print idx, val


def demo_chain():
    my_list0 = [1, 2, 3]
    my_list1 = [4, 5, 6]
    my_list2 = ['a', 'b', 'c']
    for ele in chain(my_list0, my_list1, my_list2):
        print ele


if __name__ == '__main__':
    demo_combinations()
    demo_enumeration()
    demo_chain()
