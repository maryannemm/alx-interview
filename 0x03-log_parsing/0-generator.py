#!/usr/bin/python3
"""
This script simulates log generation by writing formatted HTTP log entries to stdout.

- It generates 10,000 logs, each with a random IP address.
- Each log entry includes a timestamp, a randomly chosen HTTP status code, 
  and a random byte size.
- The script introduces random delays between log entries using `sleep()`.

Modules:
    random: Provides functions for generating random numbers.
    sys: Provides access to system-specific parameters and functions.
    time: Contains the sleep function to introduce a delay.
    datetime: Provides the `datetime.now()` function to generate timestamps.
"""

import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())  # Introduce a random delay between 0 and 1 second
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),  # Random IP address
        datetime.datetime.now(),  # Current timestamp
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),  # Random HTTP status code
        random.randint(1, 1024)  # Random byte size
    ))
    sys.stdout.flush()  # Flush output to ensure it appears immediately

