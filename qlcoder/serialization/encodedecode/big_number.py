int_value = 10 ** 5
str_value = str(int_value)
len_num = len(str_value)
len_str = str(len_num)
if (len_num < 10):
    len_str = '0' + len_str
print str_value
print len(str_value)
en_str= len_str + str_value
print en_str
