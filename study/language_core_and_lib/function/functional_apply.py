def func0(right_num):
    def func1(left_num):
        return right_num + left_num

    return func1


def demo_curry0():
    print apply(apply(func0, (111,)), (222,))


if __name__ == '__main__':
    demo_curry0()
