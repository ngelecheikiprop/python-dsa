my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}


for key in my_dict:
    print(key)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

names  = ["Alice", "Bob", "Charlie"]
marks = [85, 92, 78]


{ k : v for (k,v) in zip(names, marks)}

