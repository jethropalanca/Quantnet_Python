'''
This program builds off from the mortgage function in Exercise 1.5.7.
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
    mortgageList = list([random.randint(100000, 1000000) for i in range(int(number_mortgages))])
    print('\nList of Mortgages:', mortgageList)

    # Generate a rates list
    ratesList = list([random.uniform(2.5, 3.5)/12 for i in range(int(number_mortgages))])
    print('List of Rates:', ratesList)

    # Generate a term list
    termList = list([random.choice([180, 360]) for i in range(int(number_mortgages))])
    print('List of Terms:', termList)

    # Generate Unique Address List
    stringList = list([id_generator(6) for i in range(int(number_mortgages))])
    print('List of Addresses:', stringList)

    print('\nHere is a dict of your mortgages, in the form \'address: (mortgage value, rate, term)\', in actual values:')
    zip_val = zip(mortgageList, ratesList, termList)
    listValues = list(zip_val)

    zip_val2 = zip(stringList,listValues)
    msList = dict(zip_val2)
    # MSList = {z[0]: list(z[1:]) for z in zip(stringList, mortgageList, ratesList, termList)} ; prints a list not a tuple

    return msList
    print(msList)

# Create a function that calculates the WEIGHTED AVERAGE RATE of the mortgage pool (input parameter should be a list of mortgage tuples):
def waRCalculate(mortgage_tuple):

    # Get rates
    ratesList = [tuple[1] for tuple in mortgage_tuple]

    # Get weights
    ## Get list of mortgages
    mortgageList = [tuple[0] for tuple in mortgage_tuple]

    ## Sum of all elements
    mortgageSum = sum(mortgageList)

    ## Weights
    mortgageWeights = [value/mortgageSum for value in mortgageList]
    check = sum(mortgageWeights)

    ## Checking:
    print('Is the sum of mortgageWeights equal to 1?',check == 1)

    # Getting the Weighted Average Rate
    ## List
    productList = []
    for num1, num2 in zip(ratesList, mortgageWeights):
        productList.append(num1 * num2)

    ## Sum (Final Step)
    waR = round(sum(productList)*100,2)

    print('The weighted average rate is equal to:', waR,'%')
    return waR

# Create a function that calculates the WEIGHTED AVERAGE MATURITY (term) of the mortgage pool (input parameter should be a list of mortgage tuples):
def waMCalculate(mortgage_tuple):

    # Get rates
    termList = [tuple[2] for tuple in mortgage_tuple]

    # Get weights
    ## Get list of mortgages
    mortgageList = [tuple[0] for tuple in mortgage_tuple]

    ## Sum of all elements
    mortgageSum = sum(mortgageList)

    ## Weights
    mortgageWeights = [value/mortgageSum for value in mortgageList]
    check = sum(mortgageWeights)

    ## Checking:
    print('Is the sum of mortgageWeights equal to 1?',check == 1)

    # Getting the Weighted Average Rate
    ## List
    productList = []
    for num1, num2 in zip(termList, mortgageWeights):
        productList.append(num1 * num2)

    ## Sum (Final Step)
    waM = int(round(sum(productList),0))

    print('The weighted average maturity is equal to:', waM,'months or approximately', int(round(waM/12,0)), 'years')
    return waM

# Create a mortgage list and sort
def main():
    from pprint import pprint
    mList = mortgage(100)
    print(mList)

# placing main() here inadvertently when we already have a main() below, causes the program to loop indefinitely (recursion error)

# Extract a list of tuple values from the dict, and sort the list by descending order
    listTupleM = list(mList.values())
    print(listTupleM)

    print('\nSorted List of Tuples (Decreasing, based on Mortgage Values):')
    listTupleM.sort(key = lambda x:x[0], reverse = True)
    print(listTupleM)

# Function creation... Go back to line 46 onwards

# Print waRCalculate results:
    print('\nThe following code presents the results of the Weighted Average Rate function:')
    waRCalculate(listTupleM)

# print waMCalculate results:
    print('\nThe following code presents the results of the Weighted Average Maturity function:')
    waMCalculate(listTupleM)

# Create a new dictionary with term as the key and a list of (amount, rate) tuples for each Term Key:

    ## listTupleM (Mortgage, Rate, Term) is from mList which is a result of processing of the original Dict earlier

    print('\nCreating a dictionary in the form (Term : (amount, rate)):')

    newDict = {}

    for tupla, tuplb, key in listTupleM:
        if key not in newDict:
            newDict[key] = []
        newDict[key].append((tupla, tuplb))

    # Print newDict
    pprint(newDict)


if __name__=='__main__':
    main()