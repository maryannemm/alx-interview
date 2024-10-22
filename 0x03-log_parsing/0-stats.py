#!/usr/bin/python3
import sys

'''
Initialize counters
'''
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_codes = status_codes.keys()

def print_stats():
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    line_count = 0
    for line in sys.stdin:
        try:
            # Parse the line based on the given format
            parts = line.split()
            if len(parts) < 7:
                continue

            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update counters
            total_size += file_size
            if status_code in valid_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Every 10 lines, print the stats
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines with invalid format
            continue

except KeyboardInterrupt:
    # Print the final stats upon CTRL + C
    print_stats()
    raise

