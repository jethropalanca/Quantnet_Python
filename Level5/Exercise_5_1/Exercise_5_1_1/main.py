'''
This program asks the user to input year, month, day, hour, minute, second, microsecond (one after the other)... And applies datetime operations.
'''

import logging
import datetime

def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.debug('initializing...')

    try:
        # a. Asks the user to input year, month, day, hour, minute, second, microsecond (one after another).
        logging.info('\na. Asks the user to input year, month, day, hour, minute, second, microsecond (one after another).\n')
        year = int(input('\nPlease input year:'))
        month = int(input('Please input month:'))
        day = int(input('Please input day:'))
        hour = int(input('Please input hour:'))
        minute = int(input('Please input minute:'))
        second = int(input('Please input second:'))
        microsecond = int(input('Please input microsecond:'))

        # b. Create a datetime variable with the entered info.
        logging.info('\nb. Create a datetime variable with the entered info.')
        dt = datetime.datetime(year, month, day, hour, minute, second, microsecond)
        logging.info (f'Value of generated datetime object: {dt}')

        # c. Extract the datetime into year, month, day, hour, minutes, second, and microsecond. Display the following result (where … is the extracted value):
        logging.info('\nc. Extract the datetime into year, month, day, hour, minutes, second, and microsecond. Display the following result (where … is the extracted value):')
        logging.info(f'Year: {dt.year}')
        logging.info(f'Month: {dt.month}')
        logging.info(f'Day: {dt.day}')
        logging.info(f'Hour: {dt.hour}')
        logging.info(f'Minute: {dt.minute}')
        logging.info(f'Second: {dt.second}')
        logging.info(f'Microsecond: {dt.microsecond}')

        # d. Display the entered datetime with the following format: 2016-09-25 18:23:14:12342:
        logging.info('\nd. Display the entered datetime with the following format: 2016-09-25 18:23:14:12342')
        logging.info(dt.strftime('%Y-%m-%d %H:%M:%S:%f'))

        # e. Display the entered datetime with the following format: 2016 September 25 06:24:14:12342 PM:
        logging.info('\ne. Display the entered datetime with the following format: 2016 September 25 06:24:14:12342 PM')
        logging.info(dt.strftime('%Y %B %d %I:%M:%S:%f %p'))

        # f. Do parts d-e with the current local time.:
        logging.info('\nf. Do parts d-e with the current local time.')
        dt = datetime.datetime.now()
        dt1 = dt.strftime('%Y-%m-%d %H:%M:%S:%f')
        dt2 = dt.strftime('%Y %B %d %I:%M:%S:%f %p')
        logging.info(f'Part d with current local time: {dt1}')
        logging.info(f'Part e with current local time: {dt2}')

        # g. Do parts d-e with the current UTC time.:
        logging.info('\ng. Do parts d-e with the current UTC time.')
        dt = datetime.datetime.utcnow()
        dt1 = dt.strftime('%Y-%m-%d %H:%M:%S:%f')
        dt2 = dt.strftime('%Y %B %d %I:%M:%S:%f %p')
        logging.info(f'Part d with current UCT time: {dt1}')
        logging.info(f'Part e with current UCT time: {dt2}')


    except ValueError as wrongInput:
        logging.info(f'\nError: {wrongInput}')
        logging.error(ValueError)

    except Exception as errorGeneral:
        logging.info(f'\nException: {errorGeneral}')
        logging.exception(Exception)






#########################
if __name__ == '__main__':
    main()
