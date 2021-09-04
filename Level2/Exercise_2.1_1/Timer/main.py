'''
This program tests the Timer_Package.
'''

from Timer_Package.Timer import Timer


def main():
    # Instantiate t
    t = Timer()

    # Test class functionalities
    t.start()
    # t.setisRunning(True) - Placed inside t.start() instead.

    # Timer this
    lst = [i for i in range(10000001)]

    lst2 = []
    for value in lst:
        if value % 10 == 0:
            lst2.append(value)

    t.end()  # This stops the timer and prints the time taken.
    print(t.retrieveLastResult())
    # t.setisRunning(False) - Placed inside t.end() instead.

    # Test error for t.Start
    t.setisRunning(True)
    print('\nError Test 1: t.start() fails when timer has already been set.')
    t.start()

    # Test error for t.False
    t.setisRunning(False)
    print('\nError Test 2: t.end() failed when timer has already been stopped.')
    t.end()


#########################
if __name__ == '__main__':
    main()
