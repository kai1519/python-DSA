# 1. Store all the programming languages known to you using Set
languages = {"Python", "Java", "C", "C++", "SQL"}
print("Known programming languages:", languages)


# 2. Store your own information using a set
# (Note: sets do not maintain order and do not allow duplicate values)
my_info = {"Prantik", 21, "Male", "India"}
print("My information:", my_info)


# 3. Get the data type of a set
print("Data type of languages set:", type(languages))


# 4. Check if “Python” is present in the set
thisset = {"Java", "Python", "Django"}
if "Python" in thisset:
    print("Python is present in the set")
else:
    print("Python is not present in the set")


# 5. Add items from another set to the current set
thisset = {"Java", "Python", "SQL"}
secondset = {"C", "Cpp", "NoSQL"}
thisset.update(secondset)
print("After adding another set:", thisset)


# 6. Add elements of a list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.update(mylist)
print("After adding list elements:", thisset)


# 7. Remove last item of the given set
# (Sets are unordered, so pop() removes a random element)
thisset = {"Python", "Django", "JavaScript", "SQL"}
removed_item = thisset.pop()
print("Removed item:", removed_item)
print("Set after removal:", thisset)


# 8. Delete the set completely
tempset = {"Python", "Java"}
del tempset
print("Set deleted successfully")


# 9. Loop through the set and print values
thisset = {"Python", "Django", "JavaScript", "SQL"}
print("Looping through the set:")
for item in thisset:
    print(item)


# 10. Find the maximum and minimum value in a set
numbers = {10, 45, 2, 89, 23}
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
