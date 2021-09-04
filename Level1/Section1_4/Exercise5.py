'''
This program demonstrates the use of the abs function.
'''

def main():
    num = float(input('Please enter a negative number (do not enter letters/special characters or code fails):'))
    if num < 0:
        print('The negative number you entered is now positive:',abs(num))
    else:
        print('Please enter a negative number only.')

if __name__=='__main__':
    main()


