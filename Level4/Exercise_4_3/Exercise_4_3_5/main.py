'''
Open the file from 4) and read it. Display each line.
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
    logging.basicConfig(format='%(message)s', level=logging.INFO)
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

    logging.info('\nTime for some jokes!')
    logging.debug('\nOpening jokeBook.txt...')

    with open(cwd1, 'r') as jokeBook:
        for joke in jokeBook.readlines():
            logging.info(f'{joke}')


    logging.debug('Book has been closed automatically...')
    logging.info('\nThat has been the book of jokes! Thank you!')



#########################
if __name__ == '__main__':
    main()
