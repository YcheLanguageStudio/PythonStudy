import itertools

def get_clone_list():
    with open('read_list.txt') as ifs:
        return map(lambda ele: ele.strip(), ifs.readlines())


