#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-bubble-sort/


def maximumToys(prices, k):
    max_toys = 0
    # while True:
    #     hatSwap = False
    #     for i in range(len(prices)-1):
    #         if prices[i] > prices[i+1]:
    #             aux = prices[i+1]
    #             prices[i+1] = prices[i]
    #             prices[i] = aux
    #             hatSwap = True
    #     if not hatSwap:
    #         break
    prices.sort()
    total_price = 0
    for toy_price in prices:
        total_price += toy_price
        if (total_price > k):
            return max_toys
        else:
            max_toys += 1
    return max_toys


if __name__ == '__main__':
    prices = [3, 7, 2, 9]
    # prices = [1, 12, 5, 111, 200, 1000, 10]
    k = 15
    result = maximumToys(prices, k)
    print(result)
