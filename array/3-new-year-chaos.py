#!/bin/python3
# https://www.hackerrank.com/challenges/new-year-chaos


def minimumBribes(q, n):
    diff = 0
    for i in range(n):
        item_to_find = n - i
        correct_index = n - i - 1
        current_index = q.index(item_to_find)
        index_diff = correct_index - current_index
        diff += index_diff
        if (index_diff > 2):
            diff = 'Too chaotic'
            break
        if (index_diff > 0):
            q = q[:current_index] + q[current_index + 1:correct_index+1] + \
                [item_to_find] + q[correct_index+1:]
    return diff


if __name__ == '__main__':
    q = [2, 1, 5, 3, 4]
    n = 5
    result = minimumBribes(q, n)
    print(result)
