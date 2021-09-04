'''
This function calculates the mean of a passed-in list (version 2).
'''

def argsMean(*numberList):
    if not(all(type(value) != str for value in numberList)):
        print('This function only accepts lists containing numbers.')
    else:
        ttl = 0.0
        for num in numberList:
            ttl = ttl + num

        avg = ttl / len(numberList)
        print('Average is:' + str(avg))
        return avg


# Calculate Average
def main():
    argsMean(1.3, 4.5, 6.7, 11.2, 100, 987.6, 'A')
    argsMean(1.3, 4.5, 6.7, 11.2, 100, 987.6)

# Passing a List / Tuple using * operator
    list = [1.3, 4.5, 6.7, 11.2, 100, 987.6]
    print('\n',type(list))
    argsMean(*list)

    list = (1.3, 4.5, 6.7, 11.2, 100, 987.6)
    print('\n',type(list))
    argsMean(*list)

if __name__=='__main__':
    main()

