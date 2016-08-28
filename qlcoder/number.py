def search_num_divided_by_two_or_three(order_num):
    counter = 0
    for num in range(1, order_num * 2, 1):
        if num % 2 == 0 or num % 3 == 0:
            counter += 1
        if counter == order_num:
            return num


# another solution, 6k+1, 6k+2, 6k+3, 6k+4, 6k+5, 6k+6, k start from 0
def another_impl(order_num):
    k = order_num / 4
    remain = order_num % 4
    dict = {1: 2, 2: 3, 3: 4, 4: 6}
    return 6 * k + dict[remain]


print search_num_divided_by_two_or_three(2333)
print another_impl(2333)
