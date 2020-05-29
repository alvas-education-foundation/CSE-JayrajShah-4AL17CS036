ip = input()
low, up = 0, 0
for i in ip:
    if ord(i) >= 65 and ord(i) <= 90:
        up += 1
    if ord(i) >= 97 and ord(i) <= 122:
        low += 1

print("Upper case characters : ", up)
print("Lower case characters : ", low)
