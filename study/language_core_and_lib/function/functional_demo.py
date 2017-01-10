def demo_lambda():
    v = [3, 5, 2, 4, 18, 6, 1]
    max_v = max(enumerate(v), key=lambda x: x[1])
    print max_v


def demo_high_order_func():
    def add(x, y, f):
        return f(x) + f(y)

    print add(1, 2, lambda x: abs(x ** 3))


def demo_map():
    result = map(lambda x: x ** 2, range(5))
    print result


def demo_reduce():
    result = range(10)
    my_sum = reduce(lambda x, y: x + y, result)
    print 'sum:\t' + str(my_sum)
    my_min = reduce(lambda x, y: min(x, y), result)
    print 'min:\t' + str(my_min)
    my_max = reduce(lambda x, y: max(x, y), result)
    print 'min:\t' + str(my_max)


def demo_filter():
    filtered_result = filter(lambda x: x % 2 == 1, range(10))
    print filtered_result


def demo_zip():
    print zip(range(5), [i * 2 for i in range(2)])
    print zip(range(2), [i * 2 for i in range(5)])
    print zip(range(5), [i * 2 for i in range(5)])


def demo_sort():
    print sorted(range(10), lambda x, y: 0 if x == y else 1 if x < y else -1)


if __name__ == '__main__':
    demo_lambda()
    demo_high_order_func()

    demo_map()
    demo_filter()
    demo_reduce()
    demo_zip()

    demo_sort()
