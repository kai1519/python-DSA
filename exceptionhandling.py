a =90
try:
    b= int(input("Enter a number: "))
    c =a/b
except ValueError:
    print("Value Error")
finally:
    print(c)    