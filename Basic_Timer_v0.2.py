
   # Start

import time
import sys

print('-==BASIC TIMER==-')

while True:
    to_count = float(input('Please enter how much seconds do you wanna count: '))
    

    # Counting
    steps = int(to_count * 10)

    for i in range(steps, -1, -1):
        current = i / 10
        sys.stdout.write(f'\rTime: {current:.1f} ')
        sys.stdout.flush()
        time.sleep(0.1)

    print('\nTime is up!')
    

    # Asking for counting again
    while True:
        answer = input('Do you wanna count again? y/n: ').lower()

        if answer == 'y':
            break

        elif answer == 'n':
            print('...')
            time.sleep(2)       
            print('Closing...')
            exit()

        else:
            print('Please give a proper answer with y/n!')
            print('...')
            continue