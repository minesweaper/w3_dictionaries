my_dict = {'key1':'value1', 'key2': 'value2'}
print(my_dict)

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])

d = {'k1': 123, 'k2': [0,1,2], 'k3': {'insidekey': 100}, 'k4': ['a', 'b', 'c']}
d['k5'] = 300
d['k1'] = 'New Value'
print(d['k2'])
print(d['k3'])
print(d['k3']['insidekey'])
print(d['k2'][2])
mylist = d['k4']
letter = mylist[2]

print(letter.upper())
print(d['k4'][2].upper())

print(d.keys())
print(d.values())
print(d.items())