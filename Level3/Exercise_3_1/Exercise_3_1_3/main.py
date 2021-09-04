'''
This program creates a regular function that takes two separate lists as its parameters.
'''

def reconcileLists(listA, listB):
    '''
    Takes two separate lists as its parameters and compares their values.
    '''

    if len(listA) == len(listB) and (len(listA) != 0 and len(listB) != 0):
        # Version 1: list(map(lambda list: list[0] == list[1], zip(listA, listB)))
        # Preference for a more pythonic way via list comprehension:
        return [item[0] == item[1] for item in zip(listA, listB)]

    elif (len(listA) == 0 and len(listB) == 0):
        return 'ERROR: Both cannot be empty lists.'

    else:
        return 'ERROR: Length of the first list must EQUAL the Length of the second list.'

def main():
    list1 = [0,2,3,5,-1,2,5,4,10,6]
    list2 = [0,25,3,1,-1,4,5,3,10,5]
    list3 = [0, 25, 3, 1, -1, 4, 5, 3, 10]
    list4 = []
    list5 = []

    print('list4 vs list5: ', reconcileLists(list4, list5))
    print('list1 vs list3: ', reconcileLists(list1, list3))
    print('list1 vs list4: ', reconcileLists(list1, list4))
    print('list4 vs list5: ', reconcileLists(list4, list5))
    print('list1 vs list2: ', reconcileLists(list1, list2))

#########################
if __name__ == '__main__':
    main()
