import os, re, sys

my_dir = sys.argv[1]
match_pattern = re.compile(r'start.*')
for file_name in os.listdir(my_dir):
    if os.path.isfile(os.path.join(my_dir, file_name)) == True:
        if re.match(match_pattern, file_name):
            print file_name
            new_file_name = file_name.replace('start', 'collaboration')
            os.rename(os.path.join(my_dir, file_name), os.path.join(my_dir, new_file_name))
