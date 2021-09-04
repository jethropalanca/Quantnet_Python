'''
Write code that generates a list of 200,000 uniform random numbers, ranging from 1 to 20.
Additionally, generate 200,000 normally distributed random numbers (mu=10, sigma=7) and
200,000 lognormally distributed random numbers (mu=1, sigma=0.5). Export these lists of numbers
to a single CSV file (should have 200,000 rows and three columns):
'''

import random
import logging
import os

def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    # Set seed
    random.seed(0)

    # Generate a list of 200,000 uniform random numbers, ranging from 1 to 20.
    logging.info('(1)')
    logging.debug('Testing pull...')
    logging.info(f'Test pull: {random.uniform(1,20)}')

    logging.debug('\nGenerating List..')
    uniList = [random.uniform(1,20) for i in range(200000)]
    logging.info(f'Check Length: {len(uniList)}')


    # Generate a list of 200,000 normally distributed random numbers, with mu = 10 and sigma = 7.
    logging.info('\n(2)')
    logging.debug('Testing pull...')
    logging.info(f'Test pull: {random.normalvariate(mu=10,sigma=7)}')

    logging.debug('\nGenerating List..')
    normList = [random.normalvariate(mu=10,sigma=7) for i in range(200000)]
    logging.info(f'Check Length: {len(normList)}')


    # Generate a list of 200,000 lognormally distributed random numbers, with mu = 1 and sigma = 0.5.
    logging.info('\n(3)')
    logging.debug('Testing pull...')
    logging.info(f'Test pull: {random.lognormvariate(mu=1,sigma=0.5)}')

    logging.debug('\nGenerating List..')
    logNormList = [random.lognormvariate(mu=1,sigma=0.5) for i in range(200000)]
    logging.info(f'Check Length: {len(logNormList)}')

    # Creating the CSV File
    logging.debug('Setting up the list...')
    numList = zip(uniList, normList, logNormList)
    numList = list(numList)

    # Get directory of current folder...
    logging.debug('Setting directory for new file...')
    logging.debug('Not an issue to create a text in the same folder here unlike creating a subdirectory in the same directory (Uneditable and causes errors)...')
    logging.debug('Getting current directory...')
    rootDir = os.getcwd()

    logging.debug('Setting directory for new file...')
    dirFinal = os.path.join(rootDir, 'numList.csv')

    logging.info(f'\nFile creation complete, final file path = {dirFinal}')
    logging.debug(f'\nWriting information on loan list to {dirFinal}...')

    s = ','

    with open(dirFinal, 'w', newline='') as finalList:
        for tuple in numList:
            rowEntry = [f'{tuple[0]}',f'{tuple[1]}', f'{tuple[2]}\n']
            finalList.write(s.join(rowEntry))

    '''
        # Create a list of tuples instead...
        for list1, list2, list3 in numList:
            rowEntry = [f'{list1[i]}',f'{list2[i]}', f'{list3[i]}\n']
            finalList.write(s.join(rowEntry))
            i = i+1
    '''

    logging.debug(f'\nWriting successful...')


#########################
if __name__ == '__main__':
    main()
