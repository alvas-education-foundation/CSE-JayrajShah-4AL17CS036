a = []
n = int(input("Enter the size of list\n"))
print("Enter the list elements\n")
for i in range(n):
    num = int(input())
    a.append(num)
print("The postive numbers are\n")
for num in a:
    if(num > 0):
        print(num)
