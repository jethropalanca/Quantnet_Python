'''
This program searches your entire computer for all files of extension py. Hint: Use os.walk and
any necessary string manipulation functions.
'''

import os
import logging

def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    logging.debug('Initializing the root directory...')

    rootDir = 'C:\\'
    listofPy = []

    # Python guides...
    logging.debug('Generating list of files using the os.walk() generator...')
    logging.debug('Returns [] if blank...')

    n = 0
    for root, dirs, files in os.walk(rootDir): # creates the generator
        for file in files:
            if file[-3:] == '.py': # if statement to append only those with '.py' extension
                listofPy.append(file)
                n += 1

    logging.debug(f'Search complete, returning a list of files ending in .py with len = {len(listofPy)}...')
    print(listofPy)



#########################
if __name__ == '__main__':
    main()
