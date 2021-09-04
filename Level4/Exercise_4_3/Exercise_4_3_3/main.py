'''
Write code that searches your entire computer for all pdf files which reside in any directory (at any
level) that contains the string ‘gr’ in its name.
'''

import os
import logging

def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    logging.debug('Initializing the root directory...')

    rootDir = 'C:\\'
    listofwrdwithgr = []

    # Python guides...
    logging.debug('Generating list of files using the os.walk() generator...')
    logging.debug('Returns [] if blank...')

    n = 0
    for root, dirs, files in os.walk(rootDir): # creates the generator
        for file in files:
            if file.find('gr') != -1 and file[-4:] == '.pdf': # if statement to append only those words containing 'gr'
                listofwrdwithgr.append(file)
                n += 1

    logging.debug(f'Search complete, returning a list of files containing gr with len = {len(listofwrdwithgr)}...')
    print(listofwrdwithgr)



#########################
if __name__ == '__main__':
    main()
