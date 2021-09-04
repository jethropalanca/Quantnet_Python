'''
This program imports the math module and demonstrates the usage of many of its built-in functions.
'''

import math

def main():

    # Some info. about the math package
    print(dir(math))

    # Demonstration of 10 functions

    # 1. N Combinations function
    print('N Combinations:', math.comb(10, 2))

    # 2. Absolute Value function
    print('Absolute value is equal to',math.fabs(-5))

    # 3. Factorial function
    print('Factorial is equal to', math.factorial(65))

    # 4. Floor function
    print('Floor is equal to', math.floor(1.23565465))

    # 5. Greatest Common Divisor (GCD) function
    print('GCD is equal to', math.gcd(15,45,96,102,450))

    # 6. Least Common Multiple (LCM) function
    print('LCM is equal to', math.lcm(15,45,96,102,450))

    # 7. N Permutations function
    print('N Permutations:', math.perm(10, 2))

    # 8. Remainder function
    print('Remainder of 2781 / 7 is equal to', math.remainder(2781, 7))

    # 9. Exponents function
    print('e raised to the power of 65 is equal to', math.exp(65))

    # 10. Power function
    print('65 raised to the power of 65 is equal to', math.pow(65, 65))

if __name__=='__main__':
    main()


