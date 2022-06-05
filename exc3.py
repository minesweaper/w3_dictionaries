# Write a Python script to concatenate following dictionaries to create a new one.
#
# Sample Dictionary :
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print(new_dict)

# better solution
d = {}

for x in (dic1, dic2, dic3):
    d.update(x)

print(d)
