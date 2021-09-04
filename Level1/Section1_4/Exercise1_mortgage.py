'''
This program deals with mortgages and built-in functions.
'''

# Create the mortgage function (RNG)
def mortgage(number_mortgages):

    import random
    print('Please enter how many mortgages you want to pull for your list:')

    random.seed(1000)
    mortgageList = [random.randint(100, 1000) for i in range(int(number_mortgages))]

    print('\n','Here is a list of your mortgages (in thousands):')
    print(mortgageList)
    return mortgageList


# Create a mortgage list and sort
def main():
    mList = mortgage(100)

    miniMortgages = [i for i in mList if i < 200]
    print('\nminiMortages List:', miniMortgages)

    standardMortgages = [i for i in mList if 200 <= i <= 467]
    print('standardMortages List:', standardMortgages)

    jumboMortgages = [i for i in mList if i > 467]
    print('jumboMortages List:', jumboMortgages)


# Logic test to verify if resulting lists above do contain numbers only in the specified ranges.
    if all([i < 200 for i in miniMortgages]):
        print('\nTrue! miniMortgages contains only values below 200.')
    else:
        print('\nPlease rework. Some values are outside the range for miniMortgages.')

    if all([200 <= i <= 467 for i in standardMortgages]):
        print('True! standardMortgages contains only values from 200 to 467.')
    else:
        print('Please rework. Some values are outside the range for standardMortgages.')

    if all([i > 467 for i in jumboMortgages]):
        print('True! jumboMortgages contains only values above 467.')
    else:
        print('Please rework. Some values are outside the range for jumboMortgages.')


# Logic test to verify if resulting lists have even one number outside their specified ranges.
    if any([i > 200 for i in miniMortgages]):
        print('\nPlease rework. A value outside the range for miniMortgages was found.')
    else:
        print('\nTrue! miniMortgages does not contain a value above 200.')

    if any([i <= 200 or i >= 467 for i in standardMortgages]):
        print('Please rework. A value outside the range for standardMortgages was found.')
    else:
        print('True! standardMortgages does not contain a value less than or equal to 200, or greater than or equal to 467.')

    if any([i < 467 for i in jumboMortgages]):
        print('Please rework. A value outside the range for jumboMortgages was found.')
    else:
        print('True! jumboMortgages does not contain a value below 467.')

### Version 1
#    mortgageList = []
#    while True:
#        num = ''
#        while num == '':
#            num = input('Please input the mortgages of your mortage list (s to stop):')
#        if num!= 's':
#            try:
#                if 100 < float(num) < 1000:
#                    mortgageList.append(float(num))
#                else:
#                    print('Please do not input letters or special characters.')
#            except:
#                print('Please do not input letters or special characters.')
#        else:
#            break

if __name__=='__main__':
    main()