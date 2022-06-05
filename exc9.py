# Write a Python program to iterate over dictionaries using for loops

def iterate_dict(x):
    for key, value in x.items():
        print(key, "->", value)


d = {'Red': 1, 'Green': 2, 'Blue': 3}
iterate_dict(d)