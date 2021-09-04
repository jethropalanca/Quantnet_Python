'''
This program shows different file management functionalities.
'''

import os
import logging
import shutil

# EwyynTomato (Stack)
def listRightIndex(alist, value):
    '''
    Functions similar to rindex for strings.
    :param alist: Enter any object of type == list.
    :param value: Value to search for.
    :return:
    '''

    # Remove the negative 1 from return because I need nth place, not (n-1)th place
    return len(alist) - alist[-1::-1].index(value)


def main():
    # Hanapin Level 4 for safety
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    s = ('\\') # for splitting

    logging.info('SETUP... Get directory of current file and create new file there...')
    logging.info('Directory will be saved not in root C but in the file path of the homework (i.e. Level4)...')
    cwd = os.getcwd().split(s)
    rindex = listRightIndex(cwd, 'Level4') # Get first occurence of parent directory (where I will create the new folders, etc.)

    logging.info(f'\nlistRightIndex = {rindex}')
    logging.info(f'[:listRightIndex] is used instead of [:2] to find the location of parent directory to ensure that: (1) the code will always refer the Level4')
    logging.info(f'folder even if Exercise_4_3_1 was copied inside a deeper subdirectory within Level4 or (2) if my file is downloaded in a path')
    logging.info(f'containing another Level4 folder in its file path (i.e. C:\Level4\Any Folder\Level4\...).')


    # Set up for original path...
    # print(cwd1[0:rindex])
    logging.debug('Generating file path...')
    cwd1 = cwd[0:rindex]
    cwd1.insert(len(cwd1), 'python')
    cwd1 = ('\\').join(cwd1)
    logging.info(f'\nFile path as been set: {cwd1}')


    # a. Create a new directory
    logging.info('\na. CREATE a new directory (using variables similar to pythontutorial)')
    logging.debug('Make sure directory does not yet exist to prevent overwriting...')

    # set dir
    dir = cwd1

    if not os.path.exists(dir):
        os.mkdir(dir)
        logging.debug(f'{dir} was successfully created.')
        logging.info(f'File directory {dir} exists?. {os.path.exists(dir)}')

    # b. Rename the above directory.
    logging.info('\nb. RENAME the above directory.')

    # Set up for new path...
    logging.debug('Generating file path...')
    cwd2 = cwd[0:rindex]
    cwd2.insert(len(cwd2),'pythonNew')
    cwd2 = ('\\').join(cwd2)
    logging.info(f'Renaming is a change of file path... New file path: {cwd2}')

    # Change name
    oldPath = dir
    newPath = cwd2
    if os.path.exists(oldPath):
        os.rename(oldPath, newPath)
        logging.debug(f'{oldPath} was successfully renamed...')

        logging.info(f'{oldPath.split(s)[-1]} has been renamed to {newPath.split(s)[-1]}.')


    # c. Delete the above directory.
    logging.info('\nc. DELETE the above directory.')
    logging.info(f'Verify if the directory is empty... If yes, USE rmdir. Answer: {len(newPath) != 0}')

    if os.path.exists(newPath):
        os.rmdir(newPath) # rmdir is for empty directories
        logging.debug(f'\nDeleting {newPath}...')
        logging.info(f'\n{newPath} has been deleted.')

    logging.info(f'Verify if newPath no longer exists... {not os.path.exists(newPath)}')


    # d. Create another directory and create two text files in this directory.
    logging.info('\nd. Create another directory and create two text files in this directory.')

    # Set up for new path...
    logging.debug('Generating file path...')
    cwd3 = cwd[0:rindex]
    cwd3.insert(len(cwd3),'pythonNewImproved')
    cwd3 = ('\\').join(cwd3)
    logging.info(f'file path: {cwd3}')

    dir = cwd3

    if not os.path.exists(dir):
        logging.debug(f'Setting up {dir}...')
        os.mkdir(dir)
        logging.debug(f'{dir} was set up successfully.')
        logging.info(f'File directory {dir} exists?. {os.path.exists(dir)}')

    logging.debug('Placing text file file path into variables ...')
    txtName1 = os.path.join(cwd3, 'txtfile1.txt')
    txtName2 = os.path.join(cwd3, 'txtfile2.txt')

    logging.debug('Creating two text files...')
    with open(txtName1, 'w') as fp1:
        fp1.write('This file is no longer blank.')

    with open(txtName2, 'w') as fp2:
        fp2.write(txtName2)

    logging.debug('Document creation successful...')
    logging.info(f'Verify if the new documents exist... {os.path.exists(txtName1) and os.path.exists(txtName2)}')


    # e. Delete one of the text files from the above directory.
    logging.info('\ne. Delete one of the text files from the above directory.')
    logging.debug(f'Deleting {txtName2}...')
    os.remove(txtName2)
    logging.debug(f'{txtName2.split(s)[-1]} was successfully deleted...')
    logging.info(f'Verify if {txtName2.split(s)[-1]} was successfully deleted... {not os.path.exists(txtName2)}')


    # f. Rename the remaining text file.
    logging.info('\nf. Rename the remaining text file.')
    txtName3 = os.path.join(cwd3, 'txtfileNew.txt')

    logging.debug(f'Renaming {txtName1}...')

    if os.path.exists(txtName1):
        try:
            os.rename(txtName1, txtName3)
            logging.debug(f'{txtName3} was successfully renamed...')
            logging.info(f'{txtName1.split(s)[-1]} has been renamed to {txtName3.split(s)[-1]}.')
        except Exception as errorGeneral:
            logging.info(f'ERROR caused by running the program while shutil.rmtree was set to be a comment...')
            logging.error(f'Exception: {errorGeneral}')


    # g. Create a subdirectory within the above created directory.
    logging.info('\ng. Create a subdirectory within the above created directory.')
    cwd4 = os.path.join(cwd3, 'pythonNIsubD')

    logging.debug(f'Creating {cwd4}...')

    if os.path.exists(cwd3):
        try:
            os.mkdir(cwd4)
            logging.debug(f'{cwd4} was created...')
            logging.info(f'Verify if the new subdirectory exists... {os.path.exists(cwd4)}')
        except Exception as errorGeneral:
            logging.info(f'ERROR caused by running the program while shutil.rmtree was set to be a comment...')
            logging.error(f'Exception: {errorGeneral}')


    # h. Move the remaining text file into the subdirectory.
    logging.info('\nh. Move the remaining text file into the subdirectory.')
    textcwd = os.path.join(cwd4, txtName3.split(s)[-1])

    logging.debug(f'Placing {txtName3.split(s)[-1]} into {cwd4}...')

    if os.path.exists(cwd3):
        try:
            os.rename(txtName3, textcwd)
            logging.info(f'Verify if the file has been transferred... {os.path.exists(textcwd)}')

        except Exception as errorGeneral:
            logging.info(f'ERROR caused by running the program while shutil.rmtree was set to be a comment...')
            logging.error(f'Exception: {errorGeneral}')


    # i. Remove the top level directory with all its contents (using a single function call). Be careful!
    logging.info('\ni. Remove the top level directory with all its contents (using a single function call). Be careful!')
    logging.info(f'Check directory of new folder: {cwd3}')


    # logging.info(cwd3.split(s)[-1])
    logging.debug(f'Checking if {cwd3.split(s)[-1]} is the subdirectory you want to delete in {cwd3}... Yes!')
    logging.debug(f'If NOT, shutil.rmtree will not run...')

    if cwd3.split(s)[-1] == 'pythonNewImproved':
        shutil.rmtree(cwd3)
        logging.info(f'\nVerify if {cwd3} has been deleted... {not os.path.exists(cwd3)}')
    else:
        logging.error('CRISIS AVERTED. MAJOR ERROR IN CODE. PLEASE FIX.')


#########################
if __name__ == '__main__':
    main()
