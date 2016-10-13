import re
sum_int=0
with open('answers.txt') as fs:
    my_str = fs.readline()
    while my_str:
        my_str=fs.readline()
        if my_str.__contains__('data'):
            my_str=my_str.split(':')[1].strip()
            print  my_str
            sum_int+=int(my_str)


print sum_int