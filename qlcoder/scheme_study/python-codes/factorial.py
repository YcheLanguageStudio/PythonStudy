# recursion format
def factorial(n):
    if n == 0:
        return 1;
    else:
        return factorial(n - 1) * n;

#mickeyandkaka Impl
#将函数自身作为参数传入
def f2(fun, n):
    if n < 2:
        return 1
    else:
        return n * fun(fun, n - 1);

#mickeyandkaka Impl
#写成参数唯一，且返回值为函数的形式
def f3(fun):
    def inner(n):
        if n < 2:
            return 1
        else:
            return n * fun(fun)(n - 1)
    return inner




if __name__ == '__main__':
    print factorial(4)
    #f2 bind, the f2 and 4 as arguments
    print f2(f2, 4)
    #inner bind, the 4 argument
    print f3(f3)(4)
