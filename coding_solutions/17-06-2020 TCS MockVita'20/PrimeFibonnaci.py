

# checking a number is prime


def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False

    return True

# function to generate combination


def createCombination(lst):
    com = []
    for i in lst:
        for j in lst:
            if i != j:
                num = int(str(i)+str(j))
                if num not in com:
                    com.append(num)
    return com


# function to generate prime numbers

def generatePrime(low, high):
    # prime = []
    # for i in range(low, high + 1):
    #     if i == 2:
    #         prime.append(i)
    #     if i > 1:
    #         for n in range(2, i//2 + 2):
    #             if (i % n) == 0:
    #                 break
    #             else:
    #                 if n == i//2 + 1:
    #                     prime.append(i)
    # print(prime)

    prime = list(i for i in range(low, high+1) if isPrime(i))
    return prime


def primeCombination(lst):
    com = createCombination(lst)
    retlst = list(i for i in com if isPrime(i))
    return retlst, len(retlst)


def fibonacci(n, x, y):
    a = x
    b = y
    if n < 0:
        return 1
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


ip = list(map(int, input().split()))
n1, n2 = ip[0], ip[1]
if 2 <= n2 <= 100 and 2 <= n1 <= 100 and n2-n1 >= 35:
    lst1 = generatePrime(n1, n2)
    lst2, count = primeCombination(lst1)
    print(fibonacci(count, lst2[0], lst2[count-1]), end="")
    combi(lst1)


# print(createCombination(prime))
