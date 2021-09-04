'''
This program prints a list of ten names in the desired format.
'''


def main():
    print('Print a list of ten names you created:')
    namesList = ['Jethro', 'Stanley', 'Kim', 'Alec', 'Patricia', 'Christine', 'Mark', 'Norman', 'Renz', 'Luke']
    print(len(namesList))

    # Loop
    print('\nLooping through the Names:')
    i = 1
    while i < 11:
        for name in namesList:
            print('Name ' + str(i) + ': ' + name)
            i = i + 1

#########################
if __name__ == '__main__':
    main()
