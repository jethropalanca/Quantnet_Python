'''
Other tools:
'''

from functools import wraps
import time
import logging


# Memoize (Optimal Solution: Nabil Khaja. Will no longer attempt to re-invent the wheel.)
def memoize(f): # dict and storing values
    cache = f.cache = {} # creates a cache object within the function

    @wraps(f)
    def wrapped(*args, **kwargs): # Takes in generic arguments...
        key = str(args) + str(kwargs) # Key is parameter combinations
        logging.debug(f'Key to the cache dict: {key}')
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]
    return wrapped


# Timer
def timer(f):
    @wraps(f)
    def wrapped(*args, **kwargs): # Takes in generic arguments...
        s = time.time()
        result = f(*args, **kwargs)
        e = time.time()
        logging.info('{0}:{1:.4f} seconds'.format(f,e-s))
        # print(f'{f}: {e-s} seconds') Same thing using f-strings!
        return result

    return wrapped
