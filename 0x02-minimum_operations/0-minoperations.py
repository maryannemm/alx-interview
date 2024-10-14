#!/usr/bin/python3
'''Module for Interview Challenge
'''

def minOperations(n):
    '''Calculates the number of operations needed
    '''
    # Check if input is a valid integer greater than 1
    if not isinstance(n, int) or n < 0 or n == 1:
        return 0
    
    var = 1  # Tracks the current value
    count = 0  # Counts the number of operations
    dup = 0  # Stores the last successful multiplication value
    
    # Loop until var reaches or exceeds n
    while var < n:
        if n % var != 0:  # If n is not divisible by var, increment by dup
            var += dup
            count += 1
        else:  # If divisible, double var and increment count by 2
            dup = var
            var += dup
            count += 2
    
    # Return count if var equals n, else return 0
    return count if var == n else 0

