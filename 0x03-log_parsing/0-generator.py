#!/usr/bin/python3
import random
import sys
import datetime
from time import sleep

# Generate random log entries
for i in range(10000):
    sleep(random.random())  # Random sleep to simulate real-time logging
    ip_address = "{:d}.{:d}.{:d}.{:d}".format(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    method = "GET"
    resource = "/projects/260"
    protocol = "HTTP/1.1"
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)

    # Format the log line and write to stdout
    log_line = f"{ip_address} - [{timestamp}] \"{method} {resource} {protocol}\" {status_code} {file_size}\n"
    sys.stdout.write(log_line)
    sys.stdout.flush()

