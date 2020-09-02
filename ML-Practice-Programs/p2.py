'''
2. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
'''


def sum(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum


a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
c = int(input("Enter a number :"))
print(sum(a, b, c))
