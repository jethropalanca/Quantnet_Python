'''
This program allows you input numbers until you enter the letter s, and calculates the average for the inputted numbers.
'''

# Error:
def main():
    print('Calculate the average of a list:')
    allNumbers = []

# Loop to Enter Numbers
    while True:
        num = ''
        while num == '':
            num = input('Add a number to the list (s to stop):')
        if num!= 's':
            try:
                allNumbers.append(float(num))
            except:
                print('Please do not input letters or special characters.')
        else:
            break

# Calculate Average
    ttl = 0.0
    for num in allNumbers:
        ttl = ttl + num

    avg = ttl / len(allNumbers)

    print('Average is:' + str(avg))


if __name__=='__main__':
    main()
