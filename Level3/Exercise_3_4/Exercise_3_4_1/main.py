'''
This program opens a file and writes to it using the with statement. The with statement ensures that it closes before errorenous code can be run.
'''

def main():
    with open('regular.txt', 'w') as f: # w opens the file for writing only (see others online)
        f.write('write something') # unable to take Japanese characters 'イキガイ'

    print('Is the file closed?', f.closed)
    # print(f.closed()) wrong syntax



#########################
if __name__ == '__main__':
    main()
