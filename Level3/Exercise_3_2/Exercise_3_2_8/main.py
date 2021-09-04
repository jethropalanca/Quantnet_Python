'''
This program creates three generator expressions and uses PRODUCT to get all the combinations of the values.
'''

from itertools import chain, product

def square():
    return (n*n for n in range(100))

def helloPrint():
    return ('Hello' for l in range (100))

def printNum():
    return (num for num in range (100))

def main():
    print('Sample of using itertools.chain to attach three generator expressions together. PRINTED AS A LIST:')
    i = square()
    j = helloPrint()
    k = printNum()

    # Chaining the generators together
    results = product(i, j, k)

    # Loop:
    list = []
    for tuple in results:
        list.append(tuple)

    print(list)
    print('\nVerification (1000 x 1000 x 1000 possible combinations (mxnxp)):', len(list))

#########################
if __name__ == '__main__':
    main()
