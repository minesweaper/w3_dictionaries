# Write a Python script to merge two Python dictionaries

def merge_dict(a, b):
    c = dict()
    c = a
    c.update(b)
    return c


a = {1: 'a', 2: 'b'}
b = {3: 'c', 4: 'd'}

print(merge_dict(a,b))