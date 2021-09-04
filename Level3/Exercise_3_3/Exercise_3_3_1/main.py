'''
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
        exit()
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
        except ZeroDivisionError as error:
            print('\nDivision by Zero is UNDEFINED... Please try again.')
            print('ERROR: ', error, '.')
        except Exception as errorGeneral:
            print('\nPlease try again.')
            print('ERROR:', errorGeneral, '.')



#########################
if __name__ == '__main__':
    main()