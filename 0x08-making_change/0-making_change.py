#!/usr/bin/python3
"""Solution to the Making Change problem."""


def make_change(coins, total):
    """
    Calculate the minimum number of coins needed to reach a given total.

    Args:
        coins (list): The denominations of available coins.
        total (int): The target amount to achieve.

    Returns:
        int: The minimum number of coins needed, or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0
    remaining = total

    for coin in coins:
        if coin <= remaining:
            count = remaining // coin
            coin_count += count
            remaining -= count * coin
        if remaining == 0:
            return coin_count

    return -1

