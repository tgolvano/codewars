# DESCRIPTION:
# Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
# NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
# Example
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */
# MATHEMATICS ALGORITHMS






#my solution

import numpy as np
import math
    
def is_prime(num):    
    if (num == 2) or (num == 3) or (num == 5) or (num == 7):
        return True
    if (num == 1) or (num == -1) or (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0) or (num % 7 == 0):
        return False

    i = 1
    sup_limit = math.floor((np.sqrt(abs(num))))
    while (i <= (1 + sup_limit) / 10):
        if (num % ((i * 10) + 1)) == 0:
            return False
        elif (num % ((i * 10) + 3)) == 0:
            return False
        elif (num % ((i * 10) + 7)) == 0:
            return False
        elif (num % ((i * 10) + 9)) == 0:
            return False
        i += 1
        
    return True