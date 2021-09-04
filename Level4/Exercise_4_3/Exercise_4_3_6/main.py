'''
Open the file from 4) and append to it.
'''

import os
import logging

# EwyynTomato (Stack)
def listRightIndex(alist, value):
    '''
    Functions similar to rindex for strings.
    :param alist: Enter any object of type == list.
    :param value: Value to search for.
    :return:
    '''

    # Remove the negative 1 from return because I need nth place, not (n-1)th place
    return len(alist) - alist[-1::-1].index(value)

def main():

    logging.basicConfig(format='%(message)s', level=logging.INFO) # Set logging level to info...

    try:
        print('This program adds four jokes to our hit sensation, jokeBook!')
        print('\nWARNING: Please answer the following question truthfully else jokeBook v2 will be filled with duplicate appends.')
        print('If this is your first time running this code, please ensure that jokeBook.txt only has 6 jokes.')
        continueDecision = input('\nIs this your first time appending to this file? Please input \'yes\' or \'no\' (case-sensitive... e.g. yes). If yes, please continue...')

        if continueDecision == 'yes':
            s = ('\\') # for splitting

            logging.info('SETUP... Get directory of current file and create new file there...')
            logging.info('Directory will be saved not in root C but in the file path of the homework (i.e. Level4)...')
            cwd = os.getcwd().split(s)
            rindex = listRightIndex(cwd, 'Level4') # Get first occurence of parent directory (where I will create the new folders, etc.)

            logging.info(f'\nlistRightIndex = {rindex}')
            logging.info(f'[:listRightIndex] is used instead of [:2] to find the location of parent directory to ensure that: (1) the code will always refer the Level4')
            logging.info(f'folder even if Exercise_4_3_1 was copied inside a deeper subdirectory within Level4 or (2) if my file is downloaded in a path')
            logging.info(f'containing another Level4 folder in its file path (i.e. C:\Level4\Any Folder\Level4\...).')

            # Set up for original path...
            # print(cwd1[0:rindex])
            logging.debug('Generating file path...')
            cwd1 = cwd[0:rindex]
            logging.info(f'\nfilePath of jokeBook in list form: {cwd1}')

            logging.debug('Adding subdirectory and jokeBook to the list...')
            cwd1.insert(len(cwd1), 'Exercise_4_3')
            cwd1.insert(len(cwd1), 'Exercise_4_3_4')
            cwd1.insert(len(cwd1), 'jokeBook.txt')
            cwd1 = s.join(cwd1)

            logging.info(f'\nFile path as been set: {cwd1}')

            logging.info('\nTime to add some new jokes!')
            logging.debug('\nOpening jokeBook.txt...')
            logging.debug('\nAppending jokeBook.txt...')

            with open(cwd1, 'a') as jokeBook2:
                jokeBook2.write('What\'s the best thing about Switzerland? I don\'t know, but the flag is a big plus.')
                jokeBook2.write('\nWhy can\'t you explain puns to kleptomaniacs? They always take things literally.')
                jokeBook2.write('\nWhat did the Buddhist say to the hot dog vendor? Make me one with everything.')
                jokeBook2.write('\nWhat do you call a woman with one leg? Eileen (Mine: Took me a while too).')

            logging.debug('\njokeBook has been appended...')
            logging.info('\nSecond Edition is now ready for publishing!')

            logging.debug('Opening jokeBook...')
            logging.info('\nHere\'s an early peek...')

            with open(cwd1, 'r') as jokeBook2:
                for joke in jokeBook2.readlines():
                    logging.info(f'{joke}')

            logging.debug('Book has been closed automatically...')
            logging.info('\nThat has been the book of jokes, 2nd Edition! Thank you!')
            logging.info('Feel free to open your copy again in Exercise_4_3_4 to verify the changes...')

        else:
            logging.info('\nPlease delete jokeBook from Exercise_4_3_4, then run main.py there again, before running this code.')

    except ValueError as wrongInput:
        logging.info('\nPlease enter yes or no (case-sensitive) only...')
        logging.info(f'Error: {wrongInput}')
        logging.error(TypeError)

    except Exception as wrongGeneralInput:
        logging.info('\nPlease enter yes or no (case-sensitive) only...')
        logging.info(f'Error: {wrongGeneralInput}')
        logging.exception(Exception)

#########################
if __name__ == '__main__':
    main()
