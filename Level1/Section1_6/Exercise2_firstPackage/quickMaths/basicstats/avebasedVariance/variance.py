'''
This function calculates the variance of a passed-in list.
'''

def myVarianceFunction(numberList):
    print('\nThis function calculates the variance of a passed-in list:')

    if not(all(type(value) != str for value in numberList)):
        print('This function only accepts lists containing numbers.')
    else:
        from Section1_6.Exercise2_firstPackage.quickMaths.basicstats import average
        average = average.myAveFunction(numberList)
        numerator = 0
        for num in numberList:
            numerator = (num - average)**2 + numerator

        var = numerator / (len(numberList) - 1)
        print('Variance is: ' + str(var))
        return var
