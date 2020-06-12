# CODE BY JAYRAJ
n = int(input())
for i in range(1, n+1):
    print(str((n-i)*" ")+str(i*"*"))
for i in range(1, n+1):
    print(str((i)*" ")+str((n-i)*"*"))
