'''
This function calculates the variance of a passed-in list, accounting for degrees of freedom.
'''

def myVarianceFunction2(numberList, dof = 1):
    print('\nThis function calculates the variance of a passed-in list:')

    if not(all(type(value) != str for value in numberList)):
        print('This function only accepts lists containing numbers.')
    else:
        from Exercise3_Ave import myAveFunction
        average = myAveFunction(numberList)
        numerator = 0
        for num in numberList:
            numerator = (num - average)**2 + numerator

        var = numerator / (len(numberList) - dof)
        print('Variance is: ' + str(var))
        return var

# Calculate Average
def main():
    list = [1, 2, 3, 4, 5]

    # Default dof = 1
    print('\nVariance if dof is set to default/1')
    myVarianceFunction2(list)

    print('\nVariance if dof is set to 0')
    # dof set to = 0
    myVarianceFunction2(list,0)

if __name__=='__main__':
    main()

