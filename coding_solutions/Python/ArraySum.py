a = []
n = int(input("Enter the size of array\n"))
print("Enter the array elements\n")
for i in range(n):
    num = int(input())
    a.append(num)
print("The sum is = ", sum(a))
