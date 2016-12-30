def demo_map_usage():
    my_list = {1, 2, 3}
    my_list2 = {1, 2, 4}
    my_list3 = range(10)
    print map(lambda ele: my_list3[ele], my_list & my_list2)
    # syntax sugar
    print [my_list3[ele] for ele in my_list & my_list2]


if __name__ == '__main__':
    demo_map_usage()
