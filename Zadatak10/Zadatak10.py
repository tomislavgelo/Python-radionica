import random
import time

while True:
    i = random.randint(1,100)

    if i <= 20:
        print('1\n')
    else:
        print('0\n')

    time.sleep(2)