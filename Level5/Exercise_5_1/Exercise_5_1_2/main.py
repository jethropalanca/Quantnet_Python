'''
Modify the program in 5_1_1 to request the user enter the date in the following format (for example):
2016-09-25 18:23:14:12342.
'''

import logging
import datetime

def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.debug('initializing...')

    try:
        # a. Asks the user to input year, month, day, hour, minute, second, microsecond (one after another).
        logging.info('\na. Please the a date in the following format: YYYY-mm-dd h:m:s:ms.\n')
        date = input('Please the a date in the following format: YYYY-mm-dd h:m:s:ms (e.g. 2016-09-25 18:23:14:12342).')

        # b. Create a datetime variable with the entered info.
        logging.info('\nb. Create a datetime variable with the entered info.')
        dt = datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S:%f')
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
        logging.info(f'\nError: {wrongInput}. Please try again in the correct format (e.g. 2016-09-25 18:23:14:12342)')
        logging.error(ValueError)

    except Exception as errorGeneral:
        logging.info(f'\nException: {errorGeneral}')
        logging.exception(Exception)






#########################
if __name__ == '__main__':
    main()
