# https://www.hackerrank.com/challenges/minimum-swaps-2/
# partial


def arrayManipulation(n, queries):
    arr = [0]*n

    # print(arr)
    for query in queries:
        # print('query', query)

        for i in range(query[0]-1, query[1]):
            # print('i', i)
            arr[i] = arr[i] + query[2]

        # print(arr)
    return max(arr)


if __name__ == '__main__':
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    n = 5
    result = arrayManipulation(n, queries)
    print(result)
