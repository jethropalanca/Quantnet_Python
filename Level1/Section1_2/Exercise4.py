'''
This program creates a list of all odd integers (via loop), 1-1000, and prints all numbers in the above list, separated by commas.
'''

def main():
    list_odd = []
    for i in range(1000):
        if i%2 != 0:
            list_odd.append(i)

    print(list_odd)

if __name__=='__main__':
    main()
