from collections import defaultdict


def demo_default_dict():
    members = [
        ['male', 'John'],
        ['male', 'Jack'],
        ['female', 'Lily'],
        ['male', 'Pony'],
        ['female', 'Lucy'],
    ]

    # if we want to access l-value, use result[sex]=list() for non-existing key
    result = defaultdict(list)

    # unpack is similar to c++ std::tuple with std::tie
    for sex, name in members:
        result[sex].append(name)

    print result


if __name__ == '__main__':
    demo_default_dict()
