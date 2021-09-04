'''
This function can print out the day of the week for a given number.
'''


def dayNumber(dayN):
    number = [1, 2, 3, 4, 5, 6, 7]
    day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    zip(number, day)

    try:

        while int(dayN) not in number:
            dayN = input('Please enter a number from 1 to 7:')

        day = [day for number, day in zip(number, day) if int(dayN) == number]
        dayTuple = (int(dayN), day[0])

        return dayTuple

    except:
        print('Please don\'t enter text.')

def main():
    print('Sample using 7 as input:',dayNumber(7))
    print(dayNumber(input('Please enter a number from 1 to 7:')))

if __name__=='__main__':
    main()


