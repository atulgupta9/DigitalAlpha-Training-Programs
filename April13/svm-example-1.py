import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
"""
print(digits.data)
print(digits.target)
print(digits.images[0])
"""
clf = svm.SVC(gamma=0.001,C=100)
X,y = digits.data[:-10], digits.target[:-10]
clf.fit(X,y)
print("Prediction:",clf.predict(digits.data[10].reshape(1,-1)))

plt.imshow(digits.images[10],cmap=plt.cm.gray_r,interpolation = "nearest")
plt.show()