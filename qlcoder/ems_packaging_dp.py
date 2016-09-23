package_dict=dict()
number_list=range(1,16);
kg_list=[509, 838, 924, 650, 604, 793,564, 651, 697, 649, 747, 787, 701, 605, 644]

if __name__=='__main__':
    for i in range(0, 15):
        package_dict[number_list[i]]=kg_list[i]
    print package_dict

