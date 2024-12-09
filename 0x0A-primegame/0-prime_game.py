#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds.
    :param x: Number of rounds.
    :param nums: List of n for each round.
    :return: Name of the player with the most wins, or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    # Precompute primes up to the maximum number in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Count the total wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(primes[:n + 1])
        # Maria wins if prime_count is odd; otherwise, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(n):
    """
    Generates a list indicating primality of numbers up to n using Sieve of Eratosthenes.
    :param n: The maximum number to check for primality.
    :return: List where index i is True if i is prime, False otherwise.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False

    return sieve

