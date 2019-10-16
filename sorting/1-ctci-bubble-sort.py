#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-bubble-sort/


def countSwaps(s):
    counter = 0
    while True:
        hatSwap = False
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                aux = s[i+1]
                s[i+1] = s[i]
                s[i] = aux
                counter += 1
                hatSwap = True
        if not hatSwap:
            break
    print(f'Array is sorted in {counter} swaps.')
    print(f'First Element: {s[0]}')
    print(f'Last Element: {s[-1]}')


if __name__ == '__main__':
    a = [4, 2, 3, 1]
    countSwaps(a)
