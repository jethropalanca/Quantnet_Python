'''
Monty Hall OOP
Ask: Write a simulation of the game that empirically demonstrates the accepted solution is indeed the correct solution.
Game: Three Doors, 1 Lambo - 2 Goats.

Process:
1. Player Choose Door.
2. Host Opens One of the two doors NOT chosen (has a goat).
3. Stay or SWITCH.

HYPOTHESIS (I've heard the anwer in the past too): Switching IMPROVES the chances of getting the Lambo.
Alternate Hypothesis: (1) Doesn't Matter. (2) Worse Off.
'''

import random
import logging


class montyPlayer(object):
    '''
    The abstract player base class --
    (1) Defines the switch strategy
    (2) Contains functions to choose a door and whether or not to siwtch
    '''

    # (1) Specification: A class that defines switch strategy

    def __init__(self, choice = None, switch = None):
        self._choice = None
        self._switch = None
        # self._choice = self.chooseDoor()
        # self._switch = self.switchChoice(strategy)


    # (2) Getter/Setter Properties
    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, ichoice):
        self._choice = ichoice

    @property
    def switch(self):
        return self._switch

    @switch.setter
    def switch(self, iswitch):
        self._switch = iswitch

    # (3) Functions
    def chooseDoor(self):
        self._choice = random.randint(1, 3)
        return self._choice

    def switchChoice(self, strategy, openDoor):
        if self._choice:
            if strategy == 1 or strategy == 2:
            # More pythonic:
                finalChoice = [self._choice, openDoor]
                finalChoiceText = [f'Player has chosen to stay with Door #{self._switch}.', f'Player has chosen to switch doors... Door #{openDoor} has been selected.']

                self._switch = finalChoice[strategy-1]
                logging.debug(finalChoiceText[strategy-1])
                return self._switch

            # if strategy == 1:
            #     self._switch = self._choice
            #     logging.debug(f'Player has chosen to stay with Door #{self._switch}.')
            #     return self._switch

            # elif strategy == 2:
            #     self._switch = openDoor
            #     logging.debug(f'Player has chosen to switch doors... Door #{openDoor} has been selected.')
            #     return self._switch
            else:
                raise ValueError('You have set a number outside 1 and 2. Please try again.')

        else:
            raise Exception('You have yet to choose a door. Please try again.')