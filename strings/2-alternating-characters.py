#!/bin/python3
# https://www.hackerrank.com/challenges/alternating-characters


def alternatingCharacters(s):
    counter = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            counter += 1
    return counter


if __name__ == '__main__':
    s = 'BBBBAAB'
    result = alternatingCharacters(s)
    print(result)
