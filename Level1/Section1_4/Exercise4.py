'''
This program will find the minimum and maximum mortgage amount owed, for each mortgage sub-list.
'''

# Create a mortgage list and sort
def main():

    # Get Information from part a and b
    from Exercise1_mortgage import mortgage

    mList = mortgage(100)

    miniMortgages = [i for i in mList if i < 200]
    print('\nFor miniMortgages:')
    print('The minimum value is', min(miniMortgages))
    print('The maximum value is', max(miniMortgages))

    standardMortgages = [i for i in mList if 200 <= i <= 467]
    print('\nFor standardMortgages:')
    print('The minimum value is', min(standardMortgages))
    print('The maximum value is', max(standardMortgages))

    jumboMortgages = [i for i in mList if i > 467]
    print('\nFor jumboMortgages:')
    print('The minimum value is', min(jumboMortgages))
    print('The maximum value is', max(jumboMortgages))

if __name__=='__main__':
    main()
