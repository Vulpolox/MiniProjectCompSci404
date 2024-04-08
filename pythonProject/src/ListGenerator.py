# written by Luke and Jack

import random
import time

random.seed(time.time()) # seed the random number

# pre  -- takes no arguments
# post -- returns a list of a random size between 10 and 100 containing random integers
def randList() -> list:
    size = random.randint(10, 100) # create a random list size (10-100)
    lst = []

    for i in range(size):
        lst.append(random.randint(0, 1000))

    return lst

# pre  -- takes an integer
# post -- returns a list of the size of the specified integer containing random integers
def randListConstSize(size: int) -> list:
    lst = []

    for i in range(size):
        lst.append(random.randint(0, 1000))

    return lst

# pre  -- takes integer representing size of data
# post -- returns a list of randomly generated lists
def get_data(size: int) -> list:
    lst = []
    for i in range(size):
        lst.append(randList())
        
    return lst