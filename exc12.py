# Write a Python program to remove a key from a dictionary.


def remove_from_dict(d, x):
    if x in d:
        del d[x]


myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(myDict)
remove_from_dict(myDict, 'c')
print(myDict)
