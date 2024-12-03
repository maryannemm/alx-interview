#!/usr/bin/python3
"""
Island Perimeter
"""

def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid.

    Args:
    grid (list of list of integers): 2D grid representing the map where 1's represent land and 0's represent water.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:  # If it's land
                # Check the four neighbors: up, down, left, right
                # Up (i-1, j)
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Down (i+1, j)
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Left (i, j-1)
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right (i, j+1)
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter

