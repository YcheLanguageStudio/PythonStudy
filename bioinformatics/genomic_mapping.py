from scipy.integrate import quad
import math


def density_function(x):
    param_lambda = 0.2
    return math.exp(-param_lambda * x) * param_lambda / (1 - math.exp(-param_lambda))


def first_func(x):
    return 0.4 * density_function(80.0 / 104 - x)


def second_func(x):
    return 0.6 * density_function(120.0 / 104 - x)


def sum_first_second_func(x):
    return first_func(x) + second_func(x)


def check_correctness():
    ans0, err = quad(first_func, -24.0 / 104, 16.0 / 104)
    ans1, err = quad(sum_first_second_func, 16.0 / 104, 80.0 / 104)
    ans2, err = quad(second_func, 80.0 / 104, 120.0 / 104)

    print ans0 + ans1 + ans2


def calculate_expectation_num_islands():
    func_list = map(lambda f:
                    lambda x: f(x) * math.exp(-5 * x), [first_func, sum_first_second_func, second_func])

    ans0, err = quad(func_list[0], -24.0 / 104, 16.0 / 104)
    ans1, err = quad(func_list[1], 16.0 / 104, 80.0 / 104)
    ans2, err = quad(func_list[2], 80.0 / 104, 120.0 / 104)

    print (ans0 + ans1 + ans2) * 60000


if __name__ == '__main__':
    check_correctness()
    calculate_expectation_num_islands()
