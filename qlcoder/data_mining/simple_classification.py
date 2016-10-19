import numpy as np
from sklearn.naive_bayes import GaussianNB

training_arr = np.loadtxt('adult.txt', str, '#', ',')
testing_arr = np.loadtxt('adult_test.txt', str, '#', ',')

arr_x = np.ndarray(len(training_arr),dtype=object)
arr_y = np.ndarray(len(training_arr),dtype=object)

index=0;
for element in training_arr:
    my_arr_partial = element[0:12]
    my_arr_res = element[12]
    arr_y[index]=my_arr_res
    arr_x[index] = my_arr_partial

print len(arr_x)
print len(arr_y)

clf = GaussianNB()
clf.fit(arr_x, arr_y)
res_arr = clf.predict(testing_arr)
res = ''
for ele in res_arr:
    res += str(ele)

print res
print '\n'
