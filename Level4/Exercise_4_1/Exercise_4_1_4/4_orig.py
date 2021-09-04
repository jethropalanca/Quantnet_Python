'''
Create a program that displays name age and country of residence:
'''



def main():
    # Prompt user for name, age(integer) and country of residence.

    print('\n(1) Naive String Implementation')
    try:
        name = input('Please enter your name.')

        age = int(input('Please enter your age.'))
        if age > 0:
            pass
        else:
            raise ValueError('Exception: Please enter a number greater than 0')
        
        country = input('Please enter your country.')

    except ValueError as ageError:
        print('\nPlease input an appropriate number(integer) as age. Exiting...')

    except Exception as generalError:
        print('\nPlease input a valid name / age / country.')

    else:
        print('\n' + name + ' is ' + str(age) + ' years old and lives in ' + country + '.')




    print('\n(2) Format Flags')
    try:
        name = input('Please enter your name.')

        age = int(input('Please enter your age.'))
        if age > 0:
            pass
        else:
            raise ValueError('Exception: Please enter a number greater than 0')

        country = input('Please enter your country.')

    except ValueError as ageError:
        print('\nPlease input an appropriate number(integer) as age. Exiting...')

    except Exception as generalError:
        print('\nPlease input a valid name / age / country.')

    else:
        print('\n%s is %i years old and lives in %s.' %(name, age, country))




    print('\n(3) Format Function (with numeric placeholders)')
    try:
        name = input('Please enter your name.')

        age = int(input('Please enter your age.'))
        if age > 0:
            pass
        else:
            raise ValueError('Exception: Please enter a number greater than 0')

        country = input('Please enter your country.')

    except ValueError as ageError:
        print('\nPlease input an appropriate number(integer) as age. Exiting...')

    except Exception as generalError:
        print('\nPlease input a valid name / age / country.')

    else:
        print('\n{0} is {1} years old and lives in {2}.'.format(name, age, country))




    print('\n(4) Format Function (with keyword placeholders)')
    try:
        name = input('Please enter your name.')

        age = int(input('Please enter your age.'))
        if age > 0:
            pass
        else:
            raise ValueError('Exception: Please enter a number greater than 0')

        country = input('Please enter your country.')

    except ValueError as ageError:
        print('\nPlease input an appropriate number(integer) as age. Exiting...')

    except Exception as generalError:
        print('\nPlease input a valid name / age / country.')

    else:
        print('\nCan be in any order with kwargs (illust: ex. 1: name first, ex. 2: age first, ex. 3: country first, but NO change):') # Can now be any order
        print('{a} is {b} years old and lives in {c}.'.format(a=name, b=age, c=country))
        print('{a} is {b} years old and lives in {c}.'.format(b=age, a=name, c=country))
        print('{a} is {b} years old and lives in {c}.'.format(c=country, b=age, a=name))





    print('\n(5) f-strings')
    try:
        name = input('Please enter your name.')

        age = int(input('Please enter your age.'))
        if age > 0:
            pass
        else:
            raise ValueError('Exception: Please enter a number greater than 0')

        country = input('Please enter your country.')

    except ValueError as ageError:
        print('\nPlease input an appropriate number(integer) as age. Exiting...')

    except Exception as generalError:
        print('\nPlease input a valid name / age / country.')

    else:
        print(f'\n{name} is {age} years old and lives in {country}.')




#########################
if __name__ == '__main__':
    main()
