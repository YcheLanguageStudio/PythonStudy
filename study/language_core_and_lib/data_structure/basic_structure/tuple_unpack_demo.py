def sort_two_vertices(a, b):
    if a > b:
        return b, a
    return a, b


if __name__ == '__main__':
    print type(sort_two_vertices(1, 2))
    my_set = set()
    my_tuple = (1, 2)
    my_set.add(my_tuple)
    my_set.add(my_tuple)
    my_set.add((1, 3))
    my_set.add((1, 2))
    print my_set
