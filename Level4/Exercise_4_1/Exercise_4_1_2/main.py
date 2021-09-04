'''
Save the following Windows file-path into a string variable: C:\\Users\\Me\\Desktop\\MyTable.csv.
'''



def main():
    # Initialize...
    print('Initializing...')
    fpath = 'C:\\Users\\Me\\Desktop\\MyTable.csv'
    print('String:', fpath)

    # a. Extract the filename with extension from the path.
    print('\na. Extract the filename with extension from the path.')
    print('Filename with Extension:', fpath.split('\\')[-1])

    # b. Extract the file extension only.
    print('\nb. Extract the file extension only.')
    print('Extension:', fpath.split('\\')[-1][-3::1])

    # c. Add another folder (can name it whatever you’d like) between ‘Desktop’ and the filename.
    print('\nc. Add another folder (can name it whatever you’d like) between ‘Desktop’ and the filename.')
    fpathNew = fpath.split('\\')
    print('List:',fpathNew)

    # Adds new folder
    fpathNew.insert(4,'Another Folder')

    # Sets up join:
    s = '\\'
    print('Updated String:', s.join(fpathNew))





#########################
if __name__ == '__main__':
    main()
