#!/bin/python3
# https://www.hackerrank.com/challenges/new-year-chaos
# 100%


def minimumBribes(q, n):
    diff = 0
    try:
        for i in range(n):
            item_to_find = n - i
            correct_index = n - i - 1
            min_index = item_to_find-3 if (item_to_find-3) > 0 else 0
            current_index = q.index(item_to_find,
                                    min_index, correct_index+1)
            index_diff = correct_index - current_index
            diff += index_diff
            del q[current_index]

        return diff
    except:
        return 'Too chaotic'


if __name__ == '__main__':
    q = [2, 5, 1, 3, 4]
    n = 5
    result = minimumBribes(q, n)
    print(result)
