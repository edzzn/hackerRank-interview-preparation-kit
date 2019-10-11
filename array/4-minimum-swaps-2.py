# https://www.hackerrank.com/challenges/minimum-swaps-2/


def minimumSwaps(arr, n):
    counter = 0

    while True:
        hadChange = False
        for i, item in enumerate(arr):
            if (i+1 != item):
                aux = arr[item-1]
                arr[item-1] = item
                arr[i] = aux
                counter += 1
                hadChange = True

        if not hadChange:
            break

    return counter


if __name__ == '__main__':
    arr = [2, 3, 4, 1, 5]
    n = 5
    result = minimumSwaps(arr, n)
    print(result)
