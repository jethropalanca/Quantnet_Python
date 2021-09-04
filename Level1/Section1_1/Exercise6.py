'''
This program allows you to get the area of a triangle.
'''

def main():

    # Enter input (assumed to be numeric / only uses if statements per 1.1.6 forum thread)
    base, height = input('Please input the measurement of your triangle\'s base and height (format: base space height, e.g. 5 10.2):').split()
    side1, side2 = input('Please input the measurements of the two sides of your triangle (format: side1 space side2, e.g. 5 6.1):').split()

    # Convert to float entries
    base = float(base)
    height = float(height)
    side1 = float(side1)
    side2 = float(side2)

    if base > 0 and height > 0 and side1 > 0 and side2 > 0:
        print('\nThe measurements of the base and height of your triangle is:', base, '&', height, '.')
        print('The measurements of side 1 and side 2 of your triangle is:', side1, '&', side2, '.')

    # Test whether inputted sides pass the Triangle Inequality Theorem
        if (side1 + side2 > base) and (side1 + base > side2) and (side2 + base > side1):
            area = 0.5 * base * height
            print('The area of your triangle is', area,'.')

        else:
            print('\nYour triangle is invalid as its sides violate the Triangle Inequality Theorem.')

    else:
        print('\nPlease enter valid numbers only.')


if __name__ == '__main__':
    main()