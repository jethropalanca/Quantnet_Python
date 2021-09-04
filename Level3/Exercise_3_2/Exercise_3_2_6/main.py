'''
This program creates three generator expressions and uses itertools.chain to attach them together.
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
    results = chain(i, j, k)

    # Loop:
    list = []
    for item in results:
        list.append(item)

    print(list)

#########################
if __name__ == '__main__':
    main()
