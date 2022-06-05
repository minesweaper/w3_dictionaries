# Write a Python program to multiply all the items in a dictionary.

def multiply_items_dict(x):
    result = 1
    for key, value in x.items():
        result *= value
    return result


my_dict = {'data1':100,'data2':-54,'data3':247}
print(multiply_items_dict(my_dict))