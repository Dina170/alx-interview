#!/usr/bin/python3
"""Given a pile of coins of different values, determine the
   fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """determine the fewest number of coins
       needed to meet a given amount total
    """
    if total <= 0:
        return 0
    count = 0
    for coin in sorted(coins, reverse=True):
        while total - coin >= 0:
            total -= coin
            count += 1
            # print(total, count)
        if total == 0:
            return count
    return -1
