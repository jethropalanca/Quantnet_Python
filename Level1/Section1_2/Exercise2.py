'''
This program prints required information from the homework.
'''

def main():
    # Create List
    list = [1, 2, 3, 4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10]

    # Perform the following operations
    # Print first two numbers from the list (using indexing)
    print(list[0:2])

    # Display the last two numbers
    print(list[-2:])

    # Display all besides the last.
    print(list[:9])

    # Display all besides the first.
    print(list[1:])

    # Display all besides first two and last three.
    print(list[2:-3])

    # Append the number to the end of the list
    list.append(11)
    print(list)

    # Append 5 numbers to the end of the list using a single operation
    additional = [12, 13, 14, 15, 16]
    for value in additional:
        list.append(value)
    print(list)

    # Insert one number right after the third number in the list
    list.insert(3,100)
    print(list)

    # Modify the fourth-to-last number in the list
    list[-4] = 100
    print(list)

    # Display the list backwards, using splicing.
    print(list[::-1])

    # Display every second item in the list
    print(list[1::2])

    # Display every second item in the list, backwards.
    print(list[-2::-2])


if __name__=='__main__':
    main()


