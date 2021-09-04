'''
This program creates three generator expressions zips them together, and prints the results out as a list.
'''

from itertools import chain

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
    results = zip(i, j, k)

    # Loop:
    list = []
    for tuple in results:
        list.append(tuple)

    print(list)

#########################
if __name__ == '__main__':
    main()
