'''
List Comprehension that results in a list of numbers 0 through 10,000,000.
'''
import time

def main():
    lst = [i for i in range(10000001)]

    start = time.time()
    lst2 = []
    for value in lst:
        if value % 10 == 0:
            lst2.append(value)
    end = time.time()
    print('Time in seconds for Method 1 (Loop):',str(end-start))

    start = time.time()
    lst3 = [value for value in lst if value % 10 == 0]
    end = time.time()
    print('Time in seconds for Method 2 (List Comprehension):',str(end-start))

# Q. Which is Quicker?
# A. Using a list comprehension is quicker because it is more efficient than loops as it is simpler and requires less code.

if __name__=='__main__':
    main()


