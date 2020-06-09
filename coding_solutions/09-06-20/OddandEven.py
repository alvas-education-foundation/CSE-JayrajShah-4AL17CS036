lst = list(map(int, input().split()))
odd = len(list(filter(lambda x: (x % 2 == 1), lst)))
print("Odd Count : ", odd)
print("Even Count : ", (len(lst)-odd))
