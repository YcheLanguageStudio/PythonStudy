import numpy as np

import re

from sklearn.naive_bayes import GaussianNB

training_arr = np.loadtxt('adult.txt', str, '#', ',')
testing_arr = np.loadtxt('adult_test.txt', str, '#', ',')

arr_x = np.ndarray(len(training_arr))
arr_y = np.ndarray(len(training_arr))


def find_index(my_literal, my_list):
    for i in range(0, len(my_list)):
        if my_literal == my_list[i]:
            return i;
    return -1;


work_type = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay',
             'Never-worked']

education_type = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th',
                  '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']

marry_type = ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent',
              'Married-AF-spouse']

occupation_type = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial',
                   'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing',
                   'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']

role_type = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']

race_type = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']

gender_type = ['Female', 'Male']

nationality_type = ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany',
                    'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba',
                    'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal',
                    'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia',
                    'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador',
                    'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']

type_list = [work_type, education_type, marry_type, occupation_type, role_type, race_type, gender_type,
             nationality_type]


def transform(data_ele):
    data_ele = str(data_ele)
    nums_pat = re.compile('[0-9]+$')
    if nums_pat.match(data_ele):
        return int(data_ele)
    else:
        for ele_type in type_list:
            ret_val = find_index(data_ele, ele_type)
            if ret_val != -1:
                return ret_val
        return -1


arr_y = map(lambda ele: int(ele[12]), training_arr)
arr_x = map(lambda ele: map(lambda x: transform(x), ele[0:12]), training_arr)

testing_arr = map(lambda ele: map(lambda x: transform(x), ele[0:12]), testing_arr)

print 'arr_x len:' + str(len(arr_x))
print 'arr_y len:' + str(len(arr_y))

print arr_x[0]
print testing_arr[0]

clf = GaussianNB()
clf.fit(arr_x, arr_y)
res_arr = clf.predict(testing_arr)

print reduce(lambda x, y: str(x) + str(y), res_arr)
