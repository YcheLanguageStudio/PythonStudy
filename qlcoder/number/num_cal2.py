import urllib2
import numpy as np
from io import StringIO

d=urllib2.urlopen("http://www.qlcoder.com/download/145622513871043.txt").read().decode("utf-8")
print d
arr=np.genfromtxt(StringIO(d),delimiter=" ")
z1 = np.polyfit(arr[:,0], arr[:,1], 5)
print z1
