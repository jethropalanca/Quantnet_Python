'''
This program builds off from the mortgage function in Exercise 1.4.1.
'''

# Generate Unique String List Function:
import random
import string

def id_generator(size = 6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create the mortgage function (RNG)
def mortgage(number_mortgages):

    print('\nPlease enter how many mortgages you want to pull for your list:',number_mortgages)

    random.seed(1000)

    # Generate Mortgage list
    mortgageList = list([random.randint(100, 1000) for i in range(int(number_mortgages))])
    print(mortgageList)

    # Generate Unique Address List
    stringList = list([id_generator(6) for i in range(int(number_mortgages))])
    print(stringList)

    print('\nHere is a dict of your mortgages and their associated addresses in the form address:mortgage (in thousands):')
    zip_val = zip(stringList, mortgageList)
    dictMSList = dict(zip_val)

    print(dictMSList)
    return dictMSList


# Create a mortgage list and sort
def main():
    mList = mortgage(100)

    miniMortgages = {string: mortgage for (string, mortgage) in mList.items() if mortgage < 200}
    print('\nList of miniMortgages:')
    print(miniMortgages)

    standardMortgages = {string: mortgage for (string, mortgage) in mList.items() if 200 <= mortgage <= 467}
    print('\nList of standardMortgages:')
    print(standardMortgages)

    jumboMortgages = {string: mortgage for (string, mortgage) in mList.items() if mortgage > 467}
    print('\nList of jumboMortgages:')
    print(jumboMortgages)

# Modify a value in jumboMortgages and check if it impacts the original
    jumboMortgages['ZEOPTT'] = 100
    print('\nQ. Logic test - does the modification in the filtered list affect the original?:')
    print(jumboMortgages)
    print(mList)

    # A. No. This is because jumboMortgages is now a list and modifications to the new list do not affect the original since it is a different data type (a dictionary).

# Extract the list of amounts for each separate dict:
    print('\nExtract the list of amounts for each separate dict:')

    miniMortgagesList = list(miniMortgages.values())
    print(miniMortgagesList)

    standardMortgagesList = list(standardMortgages.values())
    print(standardMortgagesList)

    jumboMortgagesList = list(jumboMortgages.values())
    print(jumboMortgagesList)

# Modify one value in miniMortgages list:
    print('\nChange first value from 164 to 180:')
    miniMortgagesList[0] = 180
    print(miniMortgagesList)
    print(miniMortgages)
    print(mList)

    # A. No. This is because miniMortgagesList is now a list, making it independent of the miniMortgage Dict and mList Dict (dictionaries). Thus, changes on the former should not impact the latter.


if __name__=='__main__':
    main()