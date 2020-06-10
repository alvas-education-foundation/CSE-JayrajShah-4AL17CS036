"""
FIBONACII PROPERTY

(5*n2 + 4) or (5*n2 – 4)  is a perfect Square
"""
import math


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x


def isFibonacci(n):

    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)


n = int(input())

if isFibonacci(n):
    print("Number is fibonacii")
else:
    print("Number is not fibonacii")
