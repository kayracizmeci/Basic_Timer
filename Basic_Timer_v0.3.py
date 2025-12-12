# Start

import time
import sys

print('-==BASIC TIMER==-')


# Counting Function
def counting(seconds):
    steps = int(seconds * 10)

    for i in range(steps, -1, -1):
        current = i / 10
        sys.stdout.write(f'\rTime: {current:.1f} ')
        sys.stdout.flush()
        time.sleep(0.1)

    print('\nTime is up!')


# Counting
while True:
    to_count = input('Please enter how many seconds do you want to count (q to quit): ').strip()

    if to_count.lower() == 'q':
        print('Exiting...')
        break

    # Control
    if to_count.replace('.', '', 1).isdigit():
        seconds = float(to_count)

        if seconds <= 0:
            print('Please enter a positive number.')
            continue

        counting(seconds)

    else:
        print('Please enter a valid number.')
        continue