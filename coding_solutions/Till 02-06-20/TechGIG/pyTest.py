N = int(input())
sum = 0
for i in range(1, N+1):
    if i != N:
        print(i, end=" + ")
    else:
        print(i, end="= ")
    sum += i
print(sum)
