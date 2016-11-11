import numpy as np
from sklearn.naive_bayes import GaussianNB

training_arr = np.loadtxt('task7629/train.txt', str, '#', ' ')
testing_arr = np.loadtxt('task7629/check.txt', str, '#', ' ')

arr_y = map(lambda ele: int(ele[11]), training_arr)
arr_x = map(lambda ele: map(lambda x: float(x), ele[1:10]), training_arr)

testing_arr = map(lambda ele: map(lambda x: float(x), ele[1:10]), testing_arr)

print arr_x[0]
print testing_arr[0]

clf = GaussianNB()
clf.fit(arr_x, arr_y)
res_arr = clf.predict(testing_arr)

print res_arr

print reduce(lambda x, y: str(x) + str(y), res_arr)
