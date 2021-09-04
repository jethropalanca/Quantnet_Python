'''
This program tests the new Timer class, modified with generator expressions.
'''

from Exercise_3_2.Exercise_3_2_5.Timer.Timer_Package.Timer import Timer

def main():
    print('Time how long it takes to sum the square of all numbers from 0 to 5,000,000:')

    # Instantiate t
    t = Timer()

    print('\nI. Time how long it takes to list all the squares:')
    t.start()
    print([i**2 for i in range(5000000)])


    t.end()  # This stops the timer and prints the time taken.
    print(t.retrieveLastResult())

    print('\nII. Time how long it takes to list all the squares:')
    t.start()
    print(sum([i ** 2 for i in range(5000000)]))


    t.end()  # This stops the timer and prints the time taken.
    print(t.retrieveLastResult())

    # Q. Compare the total time taken to build and sum each. Which one is faster? What are the benefits of using the generator instead of the list comprehension? Why?

    # A. It takes almost half the time to sum vs. to list all the numbers. This sheds light on the benefit of using generator instead of list comprehension,
    #    as it requires less memory and computing power to display all of the results than just do a quick sum without showing the elements, so does printing
    #    each item in a list in a non-lazy evaluation vs. lazy evaluation where you only print the results you need.




#########################
if __name__ == '__main__':
    main()
