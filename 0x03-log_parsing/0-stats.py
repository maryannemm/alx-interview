#!/usr/bin/python3
"""Processes input from stdin to compute metrics.

This script tracks and reports metrics after reading every 10 lines 
or when interrupted by a keyboard signal (CTRL + C). The reported 
metrics include:
    - Cumulative file size.
    - Count of different HTTP status codes encountered.
"""

def display_metrics(total_size, code_counts):
    """Outputs the accumulated metrics.

    Args:
        total_size (int): The cumulative file size so far.
        code_counts (dict): A dictionary mapping status codes to their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(code_counts):
        print("{}: {}".format(code, code_counts[code]))

if __name__ == "__main__":
    import sys

    total_size = 0
    code_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            if line_count == 10:
                display_metrics(total_size, code_counts)
                line_count = 0

            parts = line.split()

            # Attempt to add file size (last element in line)
            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            # Attempt to count status code (second-to-last element in line)
            try:
                status_code = parts[-2]
                if status_code in valid_codes:
                    code_counts[status_code] = code_counts.get(status_code, 0) + 1
            except IndexError:
                pass

        display_metrics(total_size, code_counts)

    except KeyboardInterrupt:
        display_metrics(total_size, code_counts)
        raise

