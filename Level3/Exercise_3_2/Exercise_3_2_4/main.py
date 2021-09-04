'''
This program changes the Fibonacci sequence formula from 1.3.2 and makes it a generator.
'''

def fibonacci():
    list = [0]
    a = 0
    b = 1

    while True:
        yield a
        a,b = b,a+b

def main():
    print('\nIntroducing the new Fibonacci Sequence (with lazy eval.):')

    # Print the 1st and 2nd values of the Fibonacci Sequence
    i = fibonacci()
    print('\nPrint First Two Terms:')
    print('1  ',next(i))
    print('2  ',next(i))

    # Print until 100th
    print('\nPrint 3rd to 100th Terms:')
    c = 3
    while c < 101:
        print(c,' ',next(i))
        c += 1




#########################
if __name__ == '__main__':
    main()
