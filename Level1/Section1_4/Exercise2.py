'''
This program will look into the lengths of each list in 1.4.1.
'''

# Create a mortgage list and sort
def main():

    # Get Information from part a and b
    from Exercise1_mortgage import mortgage

    mList = mortgage(100)

    miniMortgages = [i for i in mList if i < 200]
    print('\nminiMortages List:',miniMortgages)

    standardMortgages = [i for i in mList if 200 <= i <= 467]
    print('standardMortages List:', standardMortgages)

    jumboMortgages = [i for i in mList if i > 467]
    print('jumboMortages List:', jumboMortgages)

    # Verify that lengths of each mortgage sub list, if summed, equal the length of the list in part a.
    if len(mList) == len(miniMortgages) + len(standardMortgages) + len(jumboMortgages):
        print('\nThe sum of the lengths of all three lists add up to the length of the full list in part a.')
    else:
        print('\nTry again. The sum of the lengths of all three lists do not add up to the length of the full list in part a.')



if __name__=='__main__':
    main()
