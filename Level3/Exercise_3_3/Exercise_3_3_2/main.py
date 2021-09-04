'''
Modifes 3_3_1 by specifying a Value Error as a First Line of Defense before checking for 0 and other errors.
This program takes a numerator and denominator input from the user. Quotient is then taken and the result is provided in decimal form.
'''

def quotient():
    '''
    This function takes the quotient of two inputs: a numerator and a denominator (in that order).
    '''

    # Take inputs
    print('\nTaking inputs...')
    numerator, denominator = input('Please input a numerator and a denominator (format a<space>b, e.g. 12 18). Input only \'x x\' to exit:').split()
    if numerator == 'x' and denominator == 'x':
        exit('Quotient was not calculated.')
    else:
        numerator, denominator = float(numerator), float(denominator)
        print('\nCalculating quotient...')
        # Return result
        return numerator / denominator

def main():
    result = None
    while not result:
        try:
            print('The quotient is equal to = ', quotient())
            result = 1
        except ValueError as errorValue:
            print('\nThis program cannot process Special Characters, Letters, or Spaces. Please enter numbers only... Please try again.')
            print('ERROR:', errorValue, '.')
        except ZeroDivisionError as zeroError:
            print('\nDivision by Zero is UNDEFINED... Please try again.')
            print('ERROR: ', zeroError, '.')
        except Exception as errorGeneral:
            print('\nPlease try again.')
            print('ERROR:', errorGeneral, '.')



#########################
if __name__ == '__main__':
    main()
