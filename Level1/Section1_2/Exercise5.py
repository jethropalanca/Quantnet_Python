'''
This program creates an aggregate list from 3 and 4, and prints them out depending on hw requirements.
'''

def main():
    list_even = [i for i in range(1001) if i%2 == 0]
    list_odd = [i for i in range(1000) if i%2 != 0]

    # Combine List
    list = list_even + list_odd

    # Print List
    print(list)
    # Print List (Backwards)
    print(list[::-1])

if __name__=='__main__':
    main()


