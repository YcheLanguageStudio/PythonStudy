import re

# Greedy
my_pattern = re.compile(r'[0-9]+')
my_str = 'facebookcis_17'
my_result = re.findall(my_pattern, my_str)
for element in my_result:
    print element

# Lazy
my_result = re.search(my_pattern, my_str)
for element in my_result.group():
    print element

my_str2 = "a_b_c_d_";
print my_str2.replace('_', ' ')
