#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-array-left-rotation
# Complete the rotLeft function below.


def rotLeft(a, d, n):
    temp = a[0:d]
    for i in range(n-d):
        a[i] = a[i + d]

    for i in range(d):
        a[n-d+i] = temp[i]
    return a


if __name__ == '__main__':
    a = [1, 2]
    n = 2
    d = 3
    result = rotLeft(a, d, n)
    print(result)
