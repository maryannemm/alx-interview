#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of the values of coins in possession.
        total (int): Total amount to achieve with coins.

    Returns:
        int: Fewest number of coins needed to meet total,
             or -1 if total cannot be achieved.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    remaining = total

    for coin in coins:
        if remaining <= 0:
            break
        # Use as many of the current coin as possible
        count += remaining // coin
        remaining %= coin

    # If there's remaining amount that cannot be met
    if remaining != 0:
        return -1

    return count

