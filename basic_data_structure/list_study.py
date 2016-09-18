# Simple Data Structure Usage: list
if __name__ == '__main__':
    my_list = list([None])
    my_list.append(1)
    my_list.append(1)
    for iter in range(1, 8):
        my_list.append(my_list[len(my_list) - 1] + my_list[len(my_list) - 2])

    for element in my_list:
        print element

    print 'Totoal len:' + str(len(my_list))
