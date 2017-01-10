def demo_curry0():
    def func0(right_num):
        def func1(left_num):
            return right_num + left_num

        return func1

    print apply(apply(func0, (111,)), (222,))


def demo_anonymous_lambda():
    print apply(apply(lambda x: \
                          lambda y: \
                              x + y,
                      (111,)),
                (222,))


def demo_y_combiner():
    def get_y_combiner():
        return lambda f: \
            (lambda x: apply(f, (lambda v: apply(apply(x, (x,)), (v,)),))) \
                (lambda x: apply(f, (lambda v: apply(apply(x, (x,)), (v,)),)))

    Y = get_y_combiner()
    print apply(apply(Y,
                      (lambda fact: \
                           lambda n: \
                               1 if n == 0 else fact(n - 1) * n,)),
                (5,))


if __name__ == '__main__':
    demo_curry0()
    demo_anonymous_lambda()
    demo_y_combiner()
