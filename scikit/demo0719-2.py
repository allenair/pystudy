from sklearn import datasets

boston = datasets.load_boston()

print(boston.keys())
print(boston['data'][0])