# Write a Python program to sum all the items in a dictionary.


def sum_items_dict(x):
    my_sum = 0
    for key, value in x.items():
        my_sum += value
    return my_sum


my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
print(sum_items_dict(my_dict))


# Better solution
print(sum(my_dict.values()))