'''
This program creates a list of all even integers (via loop), 1-1000, and prints all numbers in the above list, separated by commas.
'''

def main():
    list_even = []
    for i in range(1001):
        if i%2 == 0:
            list_even.append(i)

    print(list_even)

if __name__=='__main__':
    main()


