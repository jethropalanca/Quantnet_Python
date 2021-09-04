'''
This function will return the number corresponding to a day to the screen.
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