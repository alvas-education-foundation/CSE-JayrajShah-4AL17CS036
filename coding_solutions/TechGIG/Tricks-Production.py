
T = int(input())
N = []
for i in range(T):
    N.append(int(input()))
for i in range(T):
    init = 1
    days = 0
    while init <= N[i]:
        if init == N[i]:
            print(days)
            break
        else:
            if init == 1:
                init += 1
            else:
                init *= 2
            days += 1
