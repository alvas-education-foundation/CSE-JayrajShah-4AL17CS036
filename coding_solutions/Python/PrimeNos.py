start = int(input("Enter the first number\n"))
end = int(input("Enter the last number\n"))
print("The prime numbers in the given range are : \n")
for i in range(start, end+1):
    if (i > 1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i, "\n")
