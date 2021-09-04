'''
Write code that generates a list of 200,000 uniform random numbers, ranging from 1 to 20.
Additionally, generate 200,000 normally distributed random numbers (mu=10, sigma=7) and
200,000 lognormally distributed random numbers (mu=1, sigma=0.5). Export these lists of numbers
to a single CSV file (should have 200,000 rows and three columns):
'''

import random
import logging
import time
from Timer.Timer_Package.Timer import Timer
from montyHall import montyGameFile

def main():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    # Set seed
    random.seed(time.time())

    # Initialize Game
    logging.debug('Initializing game...')
    game = montyGameFile.montyGame()

    # (1) Initial Game
    logging.debug('Play sample game...')
    game.playGame(2)

    # (2) Play 10m times (Strategy 2 = switch):
    logging.debug('Test hypothesis......')
    logging.getLogger().setLevel(logging.INFO)
    logging.info('\nMain Part: Testing hypothesis.')

    random.seed(0) # Set seed for consistent results

    # Interpreting Results:
    with Timer('myTimer') as t:
        t.configureTimerDisplay('seconds')
        listResults = [game.playGame(2) for i in range(10000000)]
        print(f'The approximate probability of winning with strategy 2 = {100 * sum(listResults) / len(listResults)}%.')

    # (2b) Play 10m times (Strategy 2 = switch):
    # listResults = [game.playGame(1) for i in range(10000000)]

    # Interpreting Results:
    # print(f'The approximate probability of winning with strategy 1 = {100 * sum(listResults) / len(listResults)}%.')
    # The approximate probability of winning with strategy 1 = 33.32365%.

    # Q. Was your hypothesis correct?
    # A. Yes, indeed switching when a losing door has been opened is a winning strategy, because by then, you have a 50-50 chance of either
    #    having selected the winning door to begin with or switching to another door. Whereas this probability was 1/3rd when the game began.


#########################
if __name__ == '__main__':
    main()
