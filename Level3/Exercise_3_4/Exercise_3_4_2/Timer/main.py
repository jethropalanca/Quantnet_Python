'''
This program tests the new Timer class, modified to be a context manager, modified with generator expressions.
'''

from Exercise_3_4.Exercise_3_4_2.Timer.Timer_Package.Timer import Timer

def main():
    print('TESTING MY CONTEXT MANAGER: TIMER')
    print('Time how long it takes to sum the square of all numbers from 0 to 10000:')

    print('\nI. Time how long it takes to list all the squares:')
    try:
        with Timer('myTimer'):
            print([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorValue)
    except Exception as errorGeneral:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorGeneral)


    print('\nII. [PRESCRIBED FORMAT] Time how long it takes to list all the squares:')
    print('In seconds')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('seconds')
            print([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorValue)
    except Exception as errorGeneral:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorGeneral)


    print('\nIn minutes')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('minutes')
            print([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorValue)
    except Exception as errorGeneral:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorGeneral)


    print('\nIn hours')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('hours')
            print([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorValue)
    except Exception as errorGeneral:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorGeneral)


    print('\n(a) Error 1')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay(A)
            print([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorValue)
    except Exception as errorGeneral:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorGeneral)


    print('\n(b) Error 2')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay('x')
            print([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorValue)
    except Exception as errorGeneral:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorGeneral)


    print('\n(c) Error 3')
    try:
        with Timer('myTimer') as t:
            t.configureTimerDisplay(1,'a',4)
            print([i**2 for i in range(10000)]) # built-int display configuration
    except ValueError as errorValue:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorValue)
    except Exception as errorGeneral:
        print('Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.', errorGeneral)


    # Q. How does this new timer compare with the regular Timer class?
    # A. It allows the Timer to initialize and close with less code, and avoiding errors after the function we want to run which might
    #    prevent our Timer from ending its counter.




#########################
if __name__ == '__main__':
    main()
