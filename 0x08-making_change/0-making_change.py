#!/usr/bin/python3
"""Solution to the Making Change problem."""

def calculate_min_coins(coins, total):
    """
    Calculate the minimum number of coins needed to achieve a specific total.

    Args:
        coins (list): List of available coin denominations.
        total (int): The target total to be achieved.

    Returns:
        int: The fewest number of coins required, or -1 if it is not possible.
    """
    if total <= 0:
        return 0

    coins_used = 0
    index = 0
    coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while total > 0:
        if index >= num_coins:
            return -1
        if total >= coins[index]:
            total -= coins[index]
            coins_used += 1
        else:
            index += 1

    return coins_used

