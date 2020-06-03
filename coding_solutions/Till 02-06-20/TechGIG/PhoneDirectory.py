N = int(input())
ops = []
contacts = []
for i in range(N):
    ops.append(str(input()))
    if str(ops[i]).split()[0] == "add":
        contacts.append(str(ops[i]).split()[1])


for i in ops:
    count = 0
    if str(i).split()[0] == "fetch":
        name = str(i).split()[1]
        for c in contacts:
            if str(c).startswith(name):
                count += 1
        print(count)
