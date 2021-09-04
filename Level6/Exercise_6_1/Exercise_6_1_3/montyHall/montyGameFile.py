'''
Creating the game class (Composition)
'''

# from montyPlayerFile import montyPlayer Does not work
from montyHall.montyPlayerFile import montyPlayer
import random
import logging


class montyGame(object):
    '''
    Consists of a player object and the game logic...

    The abstract game class --
    (*) Contains the playGame function:
    1. Randomly places the price behind one of the three doors
    2. Asks its player object to choose a door
    3. Figure out which door to ‘open’ (it should be one of the two non-selected doors, but
    it must not have the prize behind it). Query the player object whether or not to
    switch to the remaining door (the player object should either always switch or
    always not switch).
    4. Check if the final chosen door is a winner or loser and return the Boolean result.
    '''

    # I.F.
    def __init__(self, player = None):
        self._player = None

    # Getters and Setters
    @property
    def player(self):
        return self.player

    @player.setter
    def player(self, iplayer):
        self._player = iplayer

    @staticmethod
    def prizePosition():
        return random.randint(1, 3)

    # Function
    def playGame(self, strategy):

        if strategy == 1:
            logging.debug(f'You have selected #{strategy}. Player will always STAY with his door.')
        else:
            logging.debug(f'You have selected #{strategy}. Player will always SWITCH doors.')

        # Instantiate Player:
        logging.debug('\nInstantiating player...')
        logging.debug('\nWELCOME TO THE GAMESHOW!')
        self._player = montyPlayer()

        # Randomly Places the prize behind one of the doors
        logging.debug('Randomly placing prize behind one of the three doors...')
        prizeLocation = self.prizePosition()

        # Ask player object to choose a door
        logging.debug('\nSelecting Door...')
        logging.debug('\nPlease choose a Door.')
        doorChoice = self._player.chooseDoor()
        logging.debug(f'Player has chosen door #{doorChoice}.')



        # Figure out which door to open (have to factor in player's choice as well)...
        ## Remove prizeLocation from possible choices
        ### prizeLocation need not be removed IF NOT INITIAL CHOICE.

        logging.debug('\nTo help you judge whether you made the right choice or not, we will be opening a door without the prize...')
        if prizeLocation == doorChoice:
            doorOpenChoices = [1, 2, 3]
            doorOpenChoices.remove(prizeLocation) # remove prize location

            ## Randomly select a door to open (Only one door remains. Prize Door and Other Door has been specified)...
            switchedDoor = random.choice(doorOpenChoices)
            logging.debug(f'Door #{switchedDoor} has been opened.')

            # Remove switchedDoor to get switchable door...
            doorOpenChoices.remove(switchedDoor)  # remove prize location

            # Prize Location = Your Original Door, And another door removed. THEREFORE remaining door is a losing door.
            switchableDoor = doorOpenChoices[0] # Last Door remaining: Removed Not Prize, Remaining is ALSO Not Prize.

        else:
            doorOpenChoices = [1, 2, 3]
            doorOpenChoices.remove(prizeLocation)  # remove prize location
            doorOpenChoices.remove(doorChoice) # remove player selected

            ## Randomly select a door to open (Only one door remains. Prize Door and Other Door has been specified)...
            switchedDoor = random.choice(doorOpenChoices)
            logging.debug(f'Door #{switchedDoor} has been opened.')

            # Remove switchedDoor to get switchable door...
            # Choose Door that is not switched to (opened) or your initial choice, THEREFORE:
            switchableDoor = prizeLocation  # Last Door remaining: Not Prize and Door With Prize already chosen, Not Prize 2 was revealed. Switch will lead to prize.



        # Query the player object whether or not to switch to the remaining door.
        ## Choose 1 to stay, Choose 2 to
        logging.debug('\nPlayer is now deciding whether to stay or not...')
        playerfinalChoice = self._player.switchChoice(strategy, switchableDoor)

        # Check if the final chosen door is a winner or a loser, and return the Boolean Result
        logging.debug(f'\nChecking if the chosen door matches the door containing the prize... {playerfinalChoice == prizeLocation}.')
        logging.debug('CONGRATULATIONS YOU HAVE WON A LAMBOURGHINI.') if playerfinalChoice == prizeLocation else logging.debug('Awww... A goat. Better luck next time!')

        return playerfinalChoice == prizeLocation


    # HAS A PLAYER... Game Logic and player object...