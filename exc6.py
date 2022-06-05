# Write a Python script to generate and print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = 5
new_dict = {}
for i in range(n+1):
    new_dict.update({i: i**2})

print(new_dict)
