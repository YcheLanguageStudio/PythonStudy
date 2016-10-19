import numpy as np
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

training_arr = np.loadtxt('adult.txt', str, '#', ',')
testing_arr = np.loadtxt('adult_test.txt', str, '#', ',')

arr_x = np.ndarray(len(training_arr))
arr_y = np.ndarray(len(training_arr))

arr_y = map(lambda ele: int(ele[12]), training_arr)
arr_x = map(lambda ele: [ele[0], ele[1]], training_arr)



print arr_x[0]
#
# print len(arr_x)
# print len(arr_y)
#
# # print arr_x
# # print arr_y
# clf = GaussianNB()
# clf.fit(arr_x, arr_y)
# res_arr = clf.predict(testing_arr)
# res = ''
# for ele in res_arr:
#     res += str(ele)
#
# print res
# print '\n'
