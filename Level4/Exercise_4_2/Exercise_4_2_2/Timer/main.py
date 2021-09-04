'''
New feature: Thresholds
New feature: Error Logs (If everything is a log, no issue)
New Feature: f strings
This program tests the new Timer class, modified to be a context manager, modified with generator expressions.
'''

from Exercise_4_2.Exercise_4_2_2.Timer.Timer_Package.Timer import Timer
import logging
import time

def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO) # Set level of logging -> INFO

    ########################################
    logging.info('TEST 1: WITHIN THRESHOLD')
    logging.info('Time how long it takes to sum the square of all numbers from 0 to 10000:')

    logging.info('\nI. Time how long it takes to list all the squares:')
    try:
        with Timer('myTimer'):
            logging.info([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorValue}')
    except Exception as errorGeneral:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorGeneral}')

    logging.info('\nII. [PRESCRIBED FORMAT] Time how long it takes to list all the squares:')
    logging.info('In seconds')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('seconds')
            logging.info([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorValue}')
    except Exception as errorGeneral:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorGeneral}')


    logging.info('\nIn minutes')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('minutes')
            logging.info([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorValue}')
    except Exception as errorGeneral:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorGeneral}')


    logging.info('\nIn hours')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('hours')
            logging.info([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorValue}')
    except Exception as errorGeneral:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorGeneral}')



    ########################################
    logging.info('\nTEST 2: OUTSIDE THRESHOLD')

    logging.info('In seconds')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('seconds')
            time.sleep(60.0000001) # 60 secs = 1 minute = .02 hours
    except ValueError as errorValue:
        logging.info(
            'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorValue}')
    except Exception as errorGeneral:
        logging.info(
            'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorGeneral}')

    logging.info('\nIn minutes')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('minutes')
            time.sleep(60.0000001) # 60 secs = 1 minute = .02 hours
    except ValueError as errorValue:
        logging.info(
            'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorValue}')
    except Exception as errorGeneral:
        logging.info(
            'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorGeneral}')

    logging.info('\nIn hours')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('hours')
            time.sleep(60.0000001) # 60 secs = 1 minute = .02 hours
    except ValueError as errorValue:
        logging.info(
            'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorValue}')
    except Exception as errorGeneral:
        logging.info(
            'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorGeneral}')

    ###############################
    logging.info('\n(a) Error 1')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay(A)
            logging.info([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorValue}')
    except Exception as errorGeneral:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorGeneral}')


    logging.info('\n(b) Error 2')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('x')
            logging.info([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorValue}')
    except Exception as errorGeneral:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorGeneral}')


    logging.info('\n(c) Error 3')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay(1,'a',4)
            logging.info([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorValue}')
    except Exception as errorGeneral:
        logging.info('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
        logging.info(f'Exception: {errorGeneral}')


    # Q. How does this new timer compare with the regular Timer class?
    # A. It allows the Timer to initialize and close with less code, and avoiding errors after the function we want to run which might
    #    prevent our Timer from ending its counter.




#########################
if __name__ == '__main__':
    main()
