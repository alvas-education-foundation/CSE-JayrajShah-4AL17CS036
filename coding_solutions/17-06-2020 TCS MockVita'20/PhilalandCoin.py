import math as m


"""
for N=5 => 1,2,3 => 3
for N=10 => 1,2,3,4 => 4
"""
# function to find minimum domination


def findDom(N):
    ret = []
    for i in N:
        ret.append(int(m.log2(i))+1)
    return ret


T = int(input())
N = []

if T >= 1 and T <= 100:
    for i in range(T):
        ip = int(input())
        if ip >= 1 and ip <= 5000:
            N.append(ip)

    for j in findDom(N):
        print(j)
