'''
This program improves on Exercise 3_1_4 by making reconcileList partials that have Break-- functions specified.
This program also uses the partial functionality to provide a lambda / function input to the function in Exercise_3_1_3.
'''

from functools import partial
import random

def reconcileLists(listA, listB, breakFn):
    '''
    Takes two separate lists as its parameters and compares their values. This is improved using the lambda functionality.
    '''

    if len(listA) == len(listB) and (len(listA) != 0 and len(listB) != 0):
        return list(map(breakFn, listA, listB))

    elif (len(listA) == 0 and len(listB) == 0):
        return 'ERROR: Both cannot be empty lists.'
    else:
        return 'ERROR: Length of the first list must EQUAL the Length of the second list.'

def breakAbsRelative(l1, l2, percent):
    # 3. Create function breakAbsRelative
    if l2!=0:
        return (abs(l1) / abs(l2) - 1) > percent
    else:
        return 'false'

def main():
    # 1 - 2. Create stored lambda breakAbsolute and breakRelative
    breakAbsolute = lambda l1, l2, epsilon: abs(l1 - l2) > epsilon
    breakRelative = lambda l1, l2, percent: l2 != 0 and (l1 / l2) - 1 > percent # expression before and fixes zerodivisionerror

    print('Epsilon and Percent Parameters have been set successfully ...')
    print('***Logic to deal with ZeroDivisionError: If denominator = 0, false.')
    print('***Please enter a POSITIVE epsilon or the test will be meaningless (all will be greater than a negative number because of abs())')
    # Set-up functools
    breakAbspartial = partial(breakAbsolute, epsilon = 40)
    breakRelpartial = partial(breakRelative, percent = 0.05)
    breakAbsRelpartial = partial(breakAbsRelative, percent = 0.05)

    reconcileListsBreakAbsolute = partial(reconcileLists, breakFn = breakAbspartial)
    reconcileListsBreakRelative = partial(reconcileLists, breakFn = breakRelpartial)
    reconcileListsBreakAbsRelative = partial(reconcileLists, breakFn = breakAbsRelpartial)

    random.seed(0)

    print('\nSet up List for breakAbsolute, breakRelative, and breakAbsRelative test...')
    # Zero Division Error present for list of integers.
    # Set-up Lists for breakAbsolute
    list1 = [round(random.uniform(-100,100),2) for i in range(10000)]
    print(list1)

    list2 = [round(random.uniform(-100,100),2) for i in range(10000)] # Exclude 0 or similarity to prevent 0 division problem.
    print(list2)

    list3 = [random.randrange(-5,5,1) for i in range(99)] # Exclude 0 or similarity to prevent 0 division problem.
    print(list3)

    list4 = []
    print(list4)

    list5 = []
    print(list5)

    print('\nTest reconcileListsBreakAbsolute:')
    # Test breakAbsolute
    print('list4 vs list5: ', reconcileListsBreakAbsolute(list4, list5))
    print('list1 vs list3: ', reconcileListsBreakAbsolute(list1, list3))
    print('list1 vs list4: ', reconcileListsBreakAbsolute(list1, list4))
    print('list4 vs list5: ', reconcileListsBreakAbsolute(list4, list5))
    print('list1 vs list2: ', reconcileListsBreakAbsolute(list1, list2))
    print('Number of True:', reconcileListsBreakAbsolute(list1, list2).count(True))

    print('\nTest reconcileListsBreakRelative:')
    # Test breakRelative
    print('list4 vs list5: ', reconcileListsBreakRelative(list4, list5))
    print('list1 vs list3: ', reconcileListsBreakRelative(list1, list3))
    print('list1 vs list4: ', reconcileListsBreakRelative(list1, list4))
    print('list4 vs list5: ', reconcileListsBreakRelative(list4, list5))
    print('list1 vs list2: ', reconcileListsBreakRelative(list1, list2))
    print('Number of True:', reconcileListsBreakRelative(list1, list2).count(True))

    print('\nTest reconcileListsBreakAbsRelative:')
    # Test breakAbsRelative
    print('list4 vs list5: ', reconcileListsBreakAbsRelative(list4, list5))
    print('list1 vs list3: ', reconcileListsBreakAbsRelative(list1, list3))
    print('list1 vs list4: ', reconcileListsBreakAbsRelative(list1, list4))
    print('list4 vs list5: ', reconcileListsBreakAbsRelative(list4, list5))
    print('list1 vs list2: ', reconcileListsBreakAbsRelative(list1, list2))
    print('Number of True:', reconcileListsBreakAbsRelative(list1, list2).count(True))

#########################
if __name__ == '__main__':
    main()
