'''
This program creates a list of unique mortgage amounts.
'''

# Create a mortgage list and sort
def mortgage(number_mortgages):

    import random
    print('Please enter how many mortgages you want to pull for your list:')

    random.seed(1000)
    mortgageList = [random.randint(100, 1000) for i in range(int(number_mortgages))]

    print('Here is a list of your mortgages (in thousands):')
    print(mortgageList)
    return mortgageList


def main():

    # Get original mortgage list, and get length.
    mList = mortgage(10000)
    a = len(mList)
    print('\n# Mortgages:', len(mList))

    # Get length of mortgage list, after converting to set.
    mList = list(set(mList))
    b = len(mList)
    print('# Unique Mortgages:', len(mList))

    # Get change (i.e. number of duplicates)
    print('The difference after transforming the list into a set is',a-b,'entities. This means there were that many duplicates in our original mortgage list.')


if __name__=='__main__':
    main()
