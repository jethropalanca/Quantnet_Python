'''
Do the same thing as Exercise 1, but this time we are going to print the distribution in the Python
shell output. You can do this using horizontal dashes (-). The naïve approach would be to print one
dash for each time a certain number appears (each number getting its own row of dashes).

Standardize using formula.
'''

import random
import logging

def generateHistogram(numberList):
    # Use Dictionaries
    barsperNumber = {}

    # SET UP
    numberList = [round(num) for num in numberList]

    # (1) Generate Frequencies for each rounded-off integer
    itemstoCount = set(numberList) # to not test EACH item
    for number in itemstoCount:
        item = number
        # Key = Unique Number, Item = Frequency
        # barsperNumber[number] = sum([1 for number in numberList])
        barsperNumber[number] = numberList.count(item) # Other option is counter

    # (2) Scaling Dict Comprehension
    # Generate histoList
    # Get maxOld and minOld
    maxOld = max(list(barsperNumber.values()))
    minOld = min(list(barsperNumber.values()))

    # Create lambda for function (neater)
    scaler = (100 - 1)/(maxOld - minOld)
    scalerfreqDist = lambda freq: (scaler * (freq - maxOld)) + 100

    histoList = {obs:scalerfreqDist(frq) for (obs, frq) in sorted(barsperNumber.items(), key = lambda tupleItem: tupleItem[0])} # Use tuple[1] to sortwith

    # (3) Print Dashes
    for obs,freq in histoList.items():
        string = '-'
        print(f'{obs}: ', f'{round(freq) * string}')

    print('\n')
    return f'\nHistogram complete...'

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


    # Generate Histogram
    # Not shown... Step 1 (Test Frequency Dict)
    logging.info(generateHistogram(uniList))
    logging.info(generateHistogram(normList))
    logging.info(generateHistogram(logNormList))



#########################
if __name__ == '__main__':
    main()
