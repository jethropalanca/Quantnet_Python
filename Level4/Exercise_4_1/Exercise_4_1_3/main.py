'''
Create a list as follows: [‘C:’, ‘Users’, ‘Me’, ‘Desktop’, ‘MyTable.csv’]. Perform the following:
'''



def main():
    # Initialize...
    print('Initializing...')
    print('\nCreated List:')
    fpathList = ['C:', 'Users', 'Me', 'Desktop', 'MyTable.csv']
    print('List:',fpathList)


    # a. Join the list together to create a valid pathname.
    print('\na. Join the list together to create a valid pathname.')

    # Sets up join:
    s = '\\'
    print('Pathname:', s.join(fpathList))

    # b. Insert another folder into the list, between ‘Desktop’ and ‘MyTable.csv’ and join the
    # resulting list to create a valid pathname.
    print('\nb. Insert another folder into the list, between ‘Desktop’ and ‘MyTable.csv’ and join the resulting list to create a valid pathname.')
    fpathList.insert(4, 'Another Folder')
    print('Updated Pathname:', s.join(fpathList)) # Uses s from earlier





#########################
if __name__ == '__main__':
    main()
