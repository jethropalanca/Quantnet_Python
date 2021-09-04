'''
New feature: LOGGING((1) Actual Input, (2) Why it's Bad, (3) What the code expects)
This class generalizes our time.time method to calculate time taken for a particular process.
'''

import time
import logging
from functools import wraps


# Memoize (Nkhaja)
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

class Timer(object):
    # Step 1: Initialization Function
    def __init__(self, name):
        self.isRunning = None
        self.startTime = 0
        self.endTime = 0
        self.timeTaken = 0
        self.name = name
        self.config = 0
        self.cnfgN = 0
        self.warnThreshold = 60 # class-level warnThreshold variable

    # MODIFICATION (Exercise 3_4_2): CONTEXT MANAGERS
    def __enter__(self):
        logging.info('\nThe timer is starting...')
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        name = self.name
        cnfgN = self.cnfgN
        config = self.config
        warnThreshold = self.warnThreshold

        if not type: # Deal with other errors:
            self.end()
            if config == 'seconds' or config == 'minutes' or config == 'hours':
                timeResult = self.retrieveLastResult()
                adjtimeResult = timeResult * cnfgN
                if timeResult > warnThreshold: # 4_2_2: If within threshold, INFO
                    logging.warning('WARNING: This process has exceeded the warning threshold...')
                    logging.warning(f'{name}: {adjtimeResult:.8f} vs. {warnThreshold * cnfgN:.8f} {config} (actual vs. threshold)')
                else: # 4_2_2: If outside threshold, warning
                    logging.info('\nThis process is within the warning threshold...')
                    logging.info(f'***{name}: {adjtimeResult:.8f} vs. {warnThreshold * cnfgN:.8f} {config} (actual vs. threshold)\n') # Initialized at the beginning, manualy re-initialized at exit for default-setting.
            else:
                raise ValueError('You have entered a wrong input. Please try again.')
        else:
            raise Exception('You have entered a wrong input. Please try again.')

    # Step 2: Getter and Setter / Properties
    # Getter and Setter Function for Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, iname):
        self._name = iname

    # Setter Function
    # Works well! Is capable of setting isRunning and prints status (Edit 1 -- Put status in def start / end)
    def setisRunning(self, runsornot):
        self.isRunning = runsornot

        # Result of function
        return self.isRunning

    # Step 3: Methods
    # Start Method (Error if already started)
    def start(self):
        if self.isRunning:
            logging.info('Error: Timer is already running.')
        else:
            self.setisRunning(True)
            self.configureTimerDisplay()
            logging.info('Timer has started running.')

            self.startTime = time.time()
            # print (self.startTime) : we are able to generate values
            return self.startTime

    # Configure Method (Set to second / minutes / hours depending on input.)
    def configureTimerDisplay(self, configure='seconds'):
        self.config = configure
        if configure == 'seconds':
            self.cnfgN = 1
            return 1
        elif configure == 'minutes':
            self.cnfgN = 1 / 60
            return 1 / 60
        elif configure == 'hours':
            self.cnfgN = (1 / 60) / 60
            return (1 / 60) / 60
            # print('Time is displaying in: ', configure, '.'). Lesson: Be careful! Doing this after return makes this code unreachable.
        else:
            raise ValueError('You have entered a wrong input. Please try again.')

    # End Method (Error if not currently running)
    def end(self):
        if self.isRunning:
            self.endTime = time.time()

            # Placing this after time.time so that only the code between start and end is being timed.
            self.setisRunning(False)
            logging.info('Timer has finished calculating and will now stop.')

            return self.endTime
        else:
            logging.info('Error: Timer is not currently running.')

    # Retrieve the last timer result
    def retrieveLastResult(self):
        return self.endTime - self.startTime