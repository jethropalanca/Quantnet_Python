'''
This program calculates the sum of the full list of mortgages.
'''

# Create a mortgage list and sort
def main():

    # Get Information from part a and b
    from Exercise1_mortgage import mortgage

    mList = mortgage(100)
    print('Total amount owed to your firm is:',sum(mList))


if __name__=='__main__':
    main()
