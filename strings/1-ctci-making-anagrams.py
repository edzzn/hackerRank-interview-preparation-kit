#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-making-anagrams


def makeAnagram(a, b):
    A = sorted(a[:])
    B = sorted(b[:])
    for l in sorted(b[:]):
        if (l in A):
            A.remove(l)
    for l in sorted(a[:]):
        if (l in B):
            B.remove(l)
    return len(A) + len(B)


if __name__ == '__main__':
    a = 'fcrxzwscanmligyxyvym'
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
    result = makeAnagram(a, b)
    print(result)
