'''
This program creates a function that calculates the factorial of an input number.
'''

def Factorial(number):
    '''
    This function calculates the factorial of an input number.
    '''

    if number < 0:
        raise ValueError('Input to number() must be a positive integer')
    elif type(number) != int:
        raise TypeError('Input to number() must be a positive integer')
    else:
        print('\nSolving for the factorial of ', number, ' ...')
        N = number
        factorial = 1
        while N > 0:
            factorial = factorial * N
            N = N - 1
        return factorial

def main():
    # Valid Input
    print('\nTesting the factorial function with a VALID INPUT...')
    try:
        print('The factorial is equal to = ', Factorial(0))
    except ValueError as errorValue1:
        print('This function cannot process negative numbers. Please enter positive numbers only... Please try again.')
        print('ERROR:', errorValue1, '.')
    except TypeError as errorValue2:
        print('This function cannot process non-integers. Please enter integers only... Please try again.')
        print('ERROR:', errorValue2, '.')

    print('\nTesting the factorial function with a VALID INPUT...')
    try:
        print('The factorial is equal to = ', Factorial(20))
    except ValueError as errorValue1:
        print('This function cannot process negative numbers. Please enter positive numbers only... Please try again.')
        print('ERROR:', errorValue1, '.')
    except TypeError as errorValue2:
        print('This function cannot process non-integers. Please enter integers only... Please try again.')
        print('ERROR:', errorValue2, '.')

    print('\nTesting the factorial function with a VALID INPUT...')
    try:
        print('The factorial is equal to = ', Factorial(5))
    except ValueError as errorValue1:
        print('This function cannot process negative numbers. Please enter positive numbers only... Please try again.')
        print('ERROR:', errorValue1, '.')
    except TypeError as errorValue2:
        print('This function cannot process non-integers. Please enter integers only... Please try again.')
        print('ERROR:', errorValue2, '.')

    # Test Negative Numbers:
    print('\nTesting the factorial function with INPUT = -1...')
    try:
        print('The factorial is equal to = ', Factorial(-1))
    except ValueError as errorValue1:
        print('This function cannot process negative numbers. Please enter positive numbers only... Please try again.')
        print('ERROR:', errorValue1, '.')
    except TypeError as errorValue2:
        print('This function cannot process non-integers. Please enter integers only... Please try again.')
        print('ERROR:', errorValue2, '.')

    # Test Positive numbers:
    print('\nTesting the factorial function with INPUT non-int...')
    try:
        print('The factorial is equal to = ', Factorial(1.23))
    except ValueError as errorValue1:
        print('This function cannot process negative numbers. Please enter positive numbers only... Please try again.')
        print('ERROR:', errorValue1, '.')
    except TypeError as errorValue2:
        print('This function cannot process non-integers. Please enter integers only... Please try again.')
        print('ERROR:', errorValue2, '.')

    # Other tests:
    print('\nTesting the factorial function...')
    try:
        print('The factorial is equal to = ', Factorial('a'))
    except ValueError as errorValue1:
        print('This function cannot process negative numbers. Please enter positive numbers only... Please try again.')
        print('ERROR:', errorValue1, '.')
    except TypeError as errorValue2:
        print('This function cannot process non-integers. Please enter integers only... Please try again.')
        print('ERROR:', errorValue2, '.')

    print('\nTesting the factorial function with an undeclared variable...')
    try:
        print('The factorial is equal to = ', Factorial(a))
    except ValueError as errorValue1:
        print('This function cannot process negative numbers. Please enter positive numbers only... Please try again.')
        print('ERROR:', errorValue1, '.')
    except TypeError as errorValue2:
        print('This function cannot process non-integers. Please enter integers only... Please try again.')
        print('ERROR:', errorValue2, '.')
    # Fix for undeclared variable
    except NameError as errorValue3:
        print('This function cannot process non-integers. Please enter positive integers only... Please try again.')
        print('ERROR:', errorValue3, '.')

    print('\nTesting with general error handling to CATCH ALL ERROR TYPES with EXCEPTION functionality...')
    try:
        print('The factorial is equal to = ', Factorial(a))
    except ValueError as errorValue1:
        print('This function cannot process negative numbers. Please enter positive numbers only... Please try again.')
        print('ERROR:', errorValue1, '.')
    except TypeError as errorValue2:
        print('This function cannot process non-integers. Please enter integers only... Please try again.')
        print('ERROR:', errorValue2, '.')
    # Fix for undeclared variable
    except Exception as errorValue3:
        print('This function only takes in positive integers... Please try again.')
        print('ERROR:', errorValue3, '.')

#########################
if __name__ == '__main__':
    main()