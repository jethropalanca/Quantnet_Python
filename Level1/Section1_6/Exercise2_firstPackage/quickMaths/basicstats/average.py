'''
This function calculates the mean of a passed-in list.
'''

def myAveFunction(numberList):
    if not(all(type(value) != str for value in numberList)):
        print('This function only accepts lists containing numbers.')
    else:
        ttl = 0.0
        for num in numberList:
            ttl = ttl + num

        avg = ttl / len(numberList)
        return avg

