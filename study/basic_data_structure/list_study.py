import copy


# Simple Data Structure Usage: list
def process_list(your_list):
    your_list[0] = 5


if __name__ == '__main__':
    my_list = list([None])
    my_list.append(1)
    my_list.append(1)
    for iter in range(1, 8):
        my_list.append(my_list[len(my_list) - 1] + my_list[len(my_list) - 2])

    for element in my_list:
        print element

    print '.....'

    for i in range(0, len(my_list)):
        print my_list[i]

    print 'Totoal len:' + str(len(my_list))

    print my_list[0]

    my_list1 = [1, 2]
    my_list3 = copy.deepcopy(my_list1)
    my_list4 = copy.copy(my_list1)
    my_list2 = my_list1
    my_list1[0] = 3
    print my_list2[0]
    process_list(my_list1)
    print my_list2[0]
    print my_list3[0]
    print my_list4[0]

    my_list=[1,2,3,4,5]
    for i in range(0,5):
        print my_list[i],

    print '\n'
    for i in range(0,5)[::-1]:
        print my_list[i],
