'''
This program creates a stored lambda function that calculates the hypotenuse of a right triangle, taking base and height as its parameter.
'''
# from math import sqrt
#
# def hypotenuse(base, height):
#     '''
#     This function takes in inputs (1) base and (2) height to calculate the hypotenuse of a right triangle.
#     '''
#     return sqrt(base**2 + height**2)

def main():
    hypotenuse = lambda base, height: (base**2 + height**2)**0.5

    print('type:', hypotenuse)
    print('\nHypotenuse for base = 3 and height = 4:', hypotenuse(3, 4))
    print('Hypotenuse for base = 1 and height = 2:', hypotenuse(1, 2))
    print('Hypotenuse for base = 5 and height = 6:', hypotenuse(5, 6))
    print('Hypotenuse for base = 7 and height = 8:', hypotenuse(7, 8))
    print('Hypotenuse for base = 1000 and height = 500000:', hypotenuse(1000, 500000))


#########################
if __name__ == '__main__':
    main()
