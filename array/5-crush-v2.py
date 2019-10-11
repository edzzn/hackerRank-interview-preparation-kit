# https://www.hackerrank.com/challenges/minimum-swaps-2/
# incomplete


def arrayManipulation(n, queries):
    # queries.sort(key=lambda x: x[0])
    # print(queries)
    # queries = [[q[0], q[1], q[2], q[1]-q[0]] for q in queries]
    # print('other sort')
    # queries.sort(key=lambda x: x[3], reverse=True)
    # print(queries)
    ranges = set()
    for q in queries:
        print('\tnext q')
        if len(ranges):
            # updatedRanges = ranges[:]
            # print('ranges', ranges)
            # print('q', q)
            null_counter = 0
            for i, r in enumerate(list(ranges)):
                # print('r', r)

                # print('r', r)
                # print('q', q)
                # print('-----')

                if q[0] > r[1] or q[1] < r[0]:
                    # print('if')
                    null_counter += 1
                elif q[0] <= r[0] and q[1] >= r[0]:
                    # empieza afuera
                    # print('1 elif')
                    # print('query', q)
                    # print('ranges', ranges)
                    ranges.discard(r)
                    if q[0] <= r[0]-1:
                        # print('add [q[0], r[0]-1, q[2]]', [q[0], r[0]-1, q[2]])
                        ranges.add((q[0], r[0]-1, q[2]))

                    if r[0] <= q[1] and q[1] <= r[1]:
                        # Esta adentro
                        # print(
                            # 'add if1 (r[0], q[1], q[2])', (r[0], q[1], r[2]+q[2]))
                        ranges.add((r[0], q[1], r[2]+q[2]))
                        # print('add if1 (q[1]+1, r[1], q[2])',
                        #   (q[1]+1, r[1], r[2]))
                        ranges.add((q[1]+1, r[1], r[2]))
                    else:
                        # Esta afuera
                        # print('add if2 (r[0], r[1], q[2])', (r[0], r[1], q[2]))
                        ranges.add((r[0], r[1], q[2]))
                        ranges.add((r[1]+1, q[1], q[2]))

                elif q[0] > r[0]:
                    # Empieza adentro
                    # print('elif')

                    ranges.discard(r)
                    if r[0] < q[0]:
                        # print('add elif1 [r[0], q[0]+1, q[2]]',
                            #   [r[0], q[0]-1, q[2]])
                        ranges.add((r[0], q[0]-1, r[2]))

                    if q[1] >= r[1]:
                        # Esta fuera
                        # print(
                            # 'add if1 (r[0], q[1], q[2])', (r[0], q[1], q[2]))
                        ranges.add((q[0], r[1], r[2]+q[2]))
                        ranges.add((r[1]+1, q[1], q[2]))
                    else:
                        ranges.add((q[0], q[1], r[2]+q[2]))
                        ranges.add((q[1]+1, r[1], q[2]))
                else:
                    print('else add', q)
                    ranges.add(tuple(q))
            # print('ranges', ranges)
            if null_counter == len(ranges):
                print('just adding')
                print((ranges))
                print((q))
                ranges.add(tuple(q))
        else:
            # print('BIG else')
            ranges.add(tuple(q))
            # print('none')
    # for i, query in enumerate(queries):
    print('final ranges', ranges)
    values = [r[2] for r in list(ranges)]

    return max(values)


if __name__ == '__main__':
    import time
    start_time = time.time()
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    queries = [
        [29, 40, 787],
        [9, 26, 219],
        [21, 31, 214],
        [8, 22, 719],
        [15, 23, 102],
        [11, 24, 83],
        [14, 22, 321],
        [5, 22, 300],
        [11, 30, 832],
        [5, 25, 29],
        [16, 24, 577],
        [3, 10, 905],
        [15, 22, 335],
        [29, 35, 254],
        [9, 20, 20],
        [33, 34, 351],
        [30, 38, 564],
        [11, 31, 969],
        [3, 32, 11],
        [29, 35, 267],
        [4, 24, 531],
        [1, 38, 892],
        [12, 18, 825],
        [25, 32, 99],
        [3, 39, 107],
        [12, 37, 131],
        [3, 26, 640],
        [8, 39, 483],
        [8, 11, 194],
        [12, 37, 502],
    ]
    n = 5
    result = arrayManipulation(n, queries)
    print(result)
    print("--- %s seconds ---" % (time.time() - start_time))
