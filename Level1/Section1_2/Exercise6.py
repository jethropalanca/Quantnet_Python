'''
This program creates a list comprehension that results in a list of the squares of all numbers 0 through 100.
'''

def main():
    list_square = [i**2 for i in range(101)]
    list_1000 = [value for value in list_square if value > 1000]
    list_even = [value for value in list_1000 if value%2 == 0]

    print(list_1000)
    print(list_even)

if __name__=='__main__':
    main()
