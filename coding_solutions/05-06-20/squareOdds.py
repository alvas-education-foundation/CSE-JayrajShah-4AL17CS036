a=[]
b=[]
n=int(input('Enter n '))
for i in range(n):
    l=int(input())
    a.append(l)
b=[x*x for x in a if x%2!=0]
print(b)