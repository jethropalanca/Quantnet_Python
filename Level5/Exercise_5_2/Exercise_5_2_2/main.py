'''
Create a decorator that memoize’s the result of a function. This decorator should be flexible enough that it can work with a function with any number of parameters.
Modify the Timer class to work as a decorator (feel free to use the provided sample code).
Per QUANTNET site, NO RELATION TO TIMER CLASS. PORT OVER CODE FROM CLASS, IN VERBATIM.

'It should be a function, separate from the class. The function should reside in the same .py file as the Timer class.'
For consistency, the memoize function was also placed in the Timer.py.
'''

import time
import logging
import os
from Exercise_5_2.Exercise_5_2_2.Timer.Timer_Package.Timer import timer, memoize, Timer

# Test Function 1
@memoize
@timer
def intenseFunction(input):
    time.sleep(input)
    return 'Done'

# Test Function 2
@memoize
@timer
def listfileswithExtension(extension):
    logging.debug('Initializing the root directory...')

    rootDir = 'C:\\'
    list = []

    # Python guides...
    logging.debug('Generating list of files using the os.walk() generator...')
    logging.debug('Returns [] if blank...')

    n = 0
    for root, dirs, files in os.walk(rootDir): # creates the generator
        for file in files:
            if file[-4:] == extension: # if statement to append only those with '.py' extension
                list.append(file)
                n += 1

    return list

# Test Function 3
@memoize
@timer
def squareLister(input):
    return [i**2 for i in range(input)]


def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    logging.info('I. Testing the first function...')
    logging.info(f'{intenseFunction(3)}')
    logging.info('\nTiming the first function after memoize...') # Need to time this again as the memoize x timer decorators are all saved in cache and only result is printed during the second run.
    with Timer('myTimer'):
        logging.info(intenseFunction(3))

    logging.info('\nII. Testing the second function...')
    extension = '.pdf' # extension needs to be of the form '. + 3 letters' (e.g. .pdf)

    logging.info(f'{listfileswithExtension(extension)}')
    logging.info('\nTiming the second function after memoize...')
    with Timer('myTimer'):
        logging.info(listfileswithExtension(extension))
    
    logging.info('\nREALIZATION: Printing of output is still NOT instantaneous even with memoize.')

    # Error Case: Not viable if printing the output itself is time-consuming. Printing output is NOT instantaneuous
    '''
    logging.info('\nIII. Testing the third function...')
    input = 5000000

    logging.info(f'{squareLister(input)}')
    logging.info('\nTiming the third function after memoize...')
    with Timer('myTimer'):
        logging.info(squareLister(input))
    '''


#########################
if __name__ == '__main__':
    main()