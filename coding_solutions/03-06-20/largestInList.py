lst = list(map(int, input().split()))
if lst[0] > lst[len(lst)-1]:
    x = lst[0]
    for n, i in enumerate(lst):
        if i != x:
            lst[n] = x
else:
    x = lst[len(lst)-1]
    for n, i in enumerate(lst):
        if i != x:
            lst[n] = x
print(lst)
