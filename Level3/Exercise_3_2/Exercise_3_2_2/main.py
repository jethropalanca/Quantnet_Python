'''
This program creates a list of 1000 numbers, converts this list into a reversed iterable, and iterates through it.
'''


def main():
    # list = [i for i in range(999, -1, -1)]
    list = [i for i in range(0, 1000, 1)]
    print('length of the list is 1000?', len(list))

    revList = reversed([i for i in range(0, 1000, 1)])
    li = iter(revList)
    print('\nSample iteration (1)', next(li))
    print('Sample iteration (2)', next(li))
    print('Sample iteration (3)', next(li))
    print('Sample iteration (4)', next(li))
    print('Sample iteration (5)', next(li))
    print('Sample iteration (6)', next(li))
    print('Sample iteration (7)', next(li))
    print('Sample iteration (8)', next(li))
    print('Sample iteration (9)', next(li))


    print('\nCheck with original list:', list[:-10:-1])


#########################
if __name__ == '__main__':
    main()
