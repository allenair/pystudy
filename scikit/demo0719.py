import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()
digital = digits.images[0]
label = digits.target[0]

print(digital)

plt.axis('off')
plt.imshow(digital, cmap=plt.get_cmap('gray_r'))
plt.show()