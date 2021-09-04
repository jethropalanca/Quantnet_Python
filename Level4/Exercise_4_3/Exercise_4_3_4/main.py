'''
Open a brand-new file and write to it (should write several lines).
'''

import os
import logging

def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    logging.debug('Not an issue to create a text in the same folder here unlike creating a subdirectory in the same directory (Uneditable and causes errors)...')
    logging.debug('Getting current directory...')
    rootDir = os.getcwd()

    logging.debug('Setting directory for new file...')
    dirFinal = os.path.join(rootDir,'jokeBook.txt')

    logging.info(f'\nInitialization complete, final file path = {dirFinal}')

    logging.debug('\nWriting several lines on the file...')
    logging.info(f'\nContext Managers will be utilized to write on the file...')

    with open(dirFinal, 'w') as file:
        file.write('It takes a lot of balls to golf the way I do.')
        file.write('\nI don\'t suffer from insanity. I enjoy every minute of it.')
        file.write('\nThe only substitute for good manners is fast reflexes.')
        file.write('\nGod grades on the cross, not the curve.')
        file.write('\nA diplomat is a man who always remembers a woman\'s birthday but never remembers her age.')
        file.write('\nI tried to explain to my 4-year-old son that it\'s perfectly normal to accidentally poop your pants, but he\'s still making fun of me.\n')

    logging.debug('\nFinished writing the lines on jokeBook...')
    logging.info(f'\njokeBook is ready for reading.')



#########################
if __name__ == '__main__':
    main()
