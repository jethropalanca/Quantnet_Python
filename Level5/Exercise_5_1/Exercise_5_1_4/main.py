'''
Creating a date calculator program...
'''

import logging
import datetime

def dateCalculator():
    logging.debug('Initializing dateCalculator...')
    logging.debug('Setting format...')
    format = ('%Y %B %d %I:%M:%S:%f %p')

    logging.debug('Taking inputs...')

    dateTime = input('\nPlease a date in the following format: YYYY mmmm dd h:m:s:ms AM/PM (e.g. 2016 September 25 06:24:14:12342 PM).')
    deltatime = input('Please a delta time in the following format: hh:mm:ss:ms (e.g. -00:25:13:0)).')

    logging.debug('\nProcessing Date Time...')
    dateTime = datetime.datetime.strptime(dateTime, format)
    logging.debug(f'Value of generated datetime object: {dateTime}')

    logging.debug('\nProcessing Delta Time...')
    if deltatime.count(':') == 3:
        logging.debug('Creating 4 values from the entered deltatime string...')
        deltatime = deltatime.split(':')

        logging.debug('Processing the 4 values to create four entries...')
        hour = float(deltatime[0])
        minute = float(deltatime[1])
        seconds = float(deltatime[2])
        microseconds = float(deltatime[3])

        logging.debug('Calculating deltatime from the inputs provide above...')
        deltatime = datetime.timedelta(hours = hour, minutes = minute, seconds = seconds, microseconds = microseconds)

        logging.debug('Calculating deltatime from the inputs provide above...')
        if str(hour).count('-')!=0:
            logging.debug('If timedelta is negative...')
            dateCalcResult = dateTime - deltatime
            dateCalcResult = dateCalcResult.strftime(format)
        else:
            logging.debug('If timedelta is positive...')
            logging.debug('Calculating deltatime from the inputs provide above...')
            dateCalcResult = dateTime + deltatime
            dateCalcResult = dateCalcResult.strftime(format)

    else:
        raise ValueError('Wrong input for deltaTime (Please follow the format of the example above), please try again...')

    return dateCalcResult

def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.debug('initializing...')

    try:
        print(f'Result: {dateCalculator()}')


    except ValueError as wrongInput:
        logging.info(f'\nError: {wrongInput}')
        logging.error(ValueError)

    except Exception as errorGeneral:
        logging.info(f'\nException: {errorGeneral}')
        logging.exception(Exception)






#########################
if __name__ == '__main__':
    main()
