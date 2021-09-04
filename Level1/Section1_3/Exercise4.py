'''
This function calculates the variance of a passed-in list.
'''

def myVarianceFunction(numberList):
    print('\nThis function calculates the variance of a passed-in list:')

    if not(all(type(value) != str for value in numberList)):
        print('This function only accepts lists containing numbers.')
    else:
        from Exercise3_Ave import myAveFunction
        average = myAveFunction(numberList)
        numerator = 0
        for num in numberList:
            numerator = (num - average)**2 + numerator

        var = numerator / (len(numberList) - 1)
        print('Variance is:' + str(var))
        return var

# Calculate Average
def main():
    list = [1, 2, 3, 4, 'A']
    myVarianceFunction(list)

    list = [1, 2, 3, 4, 5]
    myVarianceFunction(list)

if __name__=='__main__':
    main()

