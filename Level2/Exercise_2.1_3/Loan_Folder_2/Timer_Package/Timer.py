'''
This class generalizes our time.time method to calculate time taken for a particular process.
'''

import time


class Timer(object):
    # Step 1: Initialization Function
    def __init__(self):
        self.isRunning = None
        self.startTime = 0
        self.endTime = 0
        self.timeTaken = 0

    # Step 2: Getter and Setter / Properties
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
            print('Error: Timer is already running.')
        else:
            self.setisRunning(True)
            print('\nTimer has started running.')

            self.startTime = time.time()
            # print (self.startTime) : we are able to generate values
            return self.startTime

    # Configure Method (Set to second / minutes / hours depending on input.)
    def configureTimerDisplay(self):
        configure = input(
            '\nPlease enter seconds, minutes or hours to configure timer display (no space, case-sensitive):')
        if configure == 'seconds':
            print('Time is displaying in:', configure, '.')
            return 1
        elif configure == 'minutes':
            print('Time is displaying in:', configure, '.')
            return 1 / 60
        elif configure == 'hours':
            print('Time is displaying in:', configure, '.')
            return (1 / 60) / 60
            # print('Time is displaying in: ', configure, '.'). Lesson: Be careful! Doing this after return makes this code unreachable.
        else:
            print('You have entered a wrong input. Please try again.')

    # End Method (Error if not currently running)
    def end(self):
        if self.isRunning:
            self.endTime = time.time()

            # Placing this after time.time so that only the code between start and end is being timed.
            self.setisRunning(False)
            print('\nTimer has finished calculating and will now stop.')

            return self.endTime
        else:
            print('Error: Timer is not currently running.')

    # Retrieve the last timer result
    def retrieveLastResult(self):
        timeTaken = self.endTime - self.startTime
        configureDisplay = Timer.configureTimerDisplay(self)

        timeTaken = timeTaken * configureDisplay
        return timeTaken
