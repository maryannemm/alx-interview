#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        row = [1]  # Start each row with the first element as 1
        if i > 0:  # Start calculating interior elements from the second row
            last_row = triangle[i - 1]
            for j in range(1, i):
                # Each interior element is the sum of the two elements above it
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)  # End each row with the last element as 1
        triangle.append(row)
    
    return triangle

