#Start

import time
import sys

print('-==BASIC TIMER==-')
to_count = float(input('Please enter how much seconds do you wanna count: '))


#Counting
steps = int(to_count * 10)

for i in range(steps, -1, -1):
    current = i / 10
    sys.stdout.write(f'\rTime: {current:.1f} ')  
    sys.stdout.flush()
    time.sleep(0.1)


#End 
print('\nTime is up!')