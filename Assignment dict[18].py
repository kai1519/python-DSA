#1. Create and print a dictionary storing personal information
info = {
    "name": "Prantik",
    "age": 21,
    "gender": "Male",
    "city": "Delhi"
}
print("1. Personal Information Dictionary:")
print(info)
print()

print("2. Accessing items using keys:")
print("Name:", info["name"])
print("Age:", info["age"])
print("Gender:", info["gender"])
# 3. Get a list of values from the dictionarY
values_list = list(info.values())
print("3. List of values from dictionary:")
print(values_list)
print()

# 4. Change value of a specific item using key
info["age"] = 22
print("4. Dictionary after updating age:")
print(info)
print()

# 5. Print all key names one by one
print("5. Keys in the dictionary:")
for key in info.keys():
    print(key)
print()

# 6. Create a nested dictionary containing three dictionaries
students = {
    "student1": {"name": "Aman", "age": 20},
    "student2": {"name": "Riya", "age": 21},
    "student3": {"name": "Karan", "age": 22}
}
print("6. Nested Dictionary:")
print(students)
print()
# 7. Create three dictionaries and store them inside one dictionary
d1 = {"a": 10}
d2 = {"b": 20}
d3 = {"c": 30}

combined_dict = {
    "dict1": d1,
    "dict2": d2,
    "dict3": d3
}
print("7. Dictionary containing three dictionaries:")
print(combined_dict)
print()

# 8. Convert two lists into a dictionary
list1 = ["name", "age", "city"]
list2 = ["Prantik", 21, "Delhi"]

list_dict = dict(zip(list1, list2))
print("8. Dictionary created from two lists:")
print(list_dict)
print()


# 9. Merge two dictionaries
dict1 = {"x": 1, "y": 2}
dict2 = {"z": 3, "w": 4}

merged_dict = dict1 | dict2
print("9. Merged Dictionary:")
print(merged_dict)
print()


# 10. Get the key with the lowest value
sample_dict = {
    "C": 92,
    "Java": 66,
    "Python": 85
}

lowest_key = min(sample_dict, key=sample_dict.get)
print("10. Key with lowest value:")
print(lowest_key)
