# Write a Python program to iterate over dictionaries using for loops.
d = {'x': 10, 'y': 20, 'z': 30}


def iterate_in_dict(x):
    for a, b in x.items():
        print(a, '->', b)


iterate_in_dict(d)