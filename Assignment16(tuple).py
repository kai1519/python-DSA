# 1. Store multiple items in a single variable using tuple
items = ("Java", "Python", "SQL", "C")
print("1.", items)

# 2. Store only one item using tuple
single_item = ("Python",)
print("2.", single_item)

# 3. Reverse the tuple
reversed_items = items[::-1]
print("3.", reversed_items)

# 4. Swap two tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1, t2 = t2, t1
print("4.", "t1 =", t1, "t2 =", t2)

# 5. Check if all items in the tuple are the same
t3 = (5, 5, 5, 5)
all_same = all(item == t3[0] for item in t3)
print("5.", all_same)

# 6. Divide the tuple into four variables
t4 = (100, 200, 300, 400)
a, b, c, d = t4
print("6.", a, b, c, d)

# 7. Copy elements 4 and 5 into a new tuple
tuple1 = (1, 2, 3, 4, 5, 6)
new_tuple = tuple1[3:5]
print("7.", new_tuple)

# 8. Sort a tuple of tuples by the second item
tuple2 = (('a', 21), ('b', 37), ('c', 11), ('d', 29))
sorted_tuple = tuple(sorted(tuple2, key=lambda x: x[1]))
print("8.", sorted_tuple)

# 9. Print value 20 from nested tuple
tuple3 = ("Python", [10, 20, 30], (2, 4, 16))
print("9.", tuple3[1][1])

# 10. Change first item (22) of list inside tuple to 222
tuple4 = (11, [22, 33], 44, 55)
tuple4[1][0] = 222
print("10.", tuple4)
