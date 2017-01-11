def demo_inner_product():
    vec0 = range(10)
    vec1 = [i ** 2 for i in range(10)]
    print 'inner product:', reduce(lambda l, r: l + r, map(lambda ele: ele[0] * ele[1], zip(vec0, vec1)), 0)
    print 'verify:', sum([i ** 3 for i in range(10)])


if __name__ == '__main__':
    demo_inner_product()
