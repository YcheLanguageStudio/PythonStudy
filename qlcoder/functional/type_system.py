import collections

statements = list()
with open('ik_language.txt') as fs:
    statements = fs.readlines()

type_set = set()
variable_dict = dict()

statements = map(lambda e: e[0:len(e) - 2].split(' '), statements)
print statements

for statement in statements:
    if statement[0] == 'type' and statement[1] not in type_set:
        type_set.add(statement[1])
        continue
    if statement[1] == ':=' and statement[0] not in variable_dict:
        if statement[2] == "new":
            if statement[3] in type_set:
                variable_dict[statement[0]] = statement[3]
                continue
        else:
            if statement[2] in variable_dict:
                variable_dict[statement[0]] = variable_dict[statement[2]]
                continue

print type_set
print variable_dict

variable_dict = collections.OrderedDict(sorted(variable_dict.items()))

for ele in variable_dict:
    print ele

for ele in variable_dict:
    print ele + '-' + variable_dict[ele],
