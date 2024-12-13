#!/usr/bin/python3
"""
Defines the `find_winner` function to solve the Prime Game problem.
"""

def primes(limit):
    """
    Generates a list of prime numbers up to a specified limit.
    Args:
        limit (int): The maximum value for generating primes.
    Returns:
        list: A list containing all prime numbers from 1 to `limit` (inclusive).
    """
    primes_list = []
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
            primes_list.append(num)
            for multiple in range(num, limit + 1, num):
                sieve[multiple] = False
    return primes_list

def isWinner(rounds, numbers):
    """
    Determines the winner of the Prime Game based on rounds and ranges.
    Args:
        rounds (int): The number of game rounds.
        numbers (list): A list of upper bounds for each round.
    Returns:
        str: The winner's name ('Maria' or 'Ben'), or None if no clear winner.
    """
    if not rounds or not numbers or rounds == 0 or not isinstance(numbers, list):
        return None

    maria_score = 0
    ben_score = 0

    for i in range(rounds):
        primes_count = len(primes(numbers[i]))
        if primes_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    return None

