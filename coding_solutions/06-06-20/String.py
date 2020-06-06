# CODE BY JAYRAJ
st = list(map(str, input().split()))
print(len(list(i for i in st if len(i) > 1 and i[0] == i[len(i)-1])))
