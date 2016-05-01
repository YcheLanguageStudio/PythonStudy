# lambda test
v = [3, 5, 2, 4, 18, 6, 1]
max_v = max(enumerate(v), key=lambda x: x[1])
print max_v


# higher order function
def add(x, y, f):
    return f(x) + f(y)


print add(1, 2, lambda x: abs(x ** 3))


# map reduce
def f(x):
    return x * x


result = map(f, [1, 2, 3, 4, 5])
print result
my_sum = reduce(lambda x, y: x + y, result)
print 'sum:\t' + str(my_sum)
my_min = reduce(lambda x, y: min(x, y), result)
print 'min:\t' + str(my_min)
my_max = reduce(lambda x, y: max(x, y), result)
print 'min:\t' + str(my_max)


# filter
def is_odd(n):
    return n % 2 == 1


filtered_result = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
print filtered_result

# sort with lambda


print sorted([1, 2, 3, 4, 5, 6, 7, 8], lambda x, y: 1 if x < y else -1)
