'''
This program creates a list of lists of any type.
'''

def main():
    nestedList = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
    flattenedList = [item for sublist in nestedList for item in sublist]

    print(flattenedList)

if __name__=='__main__':
    main()


