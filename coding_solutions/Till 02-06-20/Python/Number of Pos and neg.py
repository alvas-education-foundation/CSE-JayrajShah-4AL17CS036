a = []
n = int(input("Enter the size of list\n"))
print("Enter the list elements\n")
for i in range(n):
    num = int(input())
    a.append(num)
c = 0
for num in a:
    if(num > 0):
        c += 1
print("Positive integers = ", c)
c = 0
for num in a:
    if(num < 0):
        c += 1
print("Negative integers = ", c)
