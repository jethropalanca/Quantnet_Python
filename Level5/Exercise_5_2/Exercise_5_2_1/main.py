'''
Modify the Timer class to work as a decorator (feel free to use the provided sample code).
Per QUANTNET site, NO RELATION TO TIMER CLASS. PORT OVER CODE FROM CLASS, IN VERBATIM.

'It should be a function, separate from the class. The function should reside in the same .py file as the Timer class.'
'''

import time
from Exercise_5_2.Exercise_5_2_1.Timer.Timer_Package.Timer import timer


# Sample Timer as a Decorator
@timer
def intenseFunction(input):
    time.sleep(input)
    return 'Done'

def main():
    print(intenseFunction(5))


    # Q. How does this compare to the previous approach to using the context manager? When is this
    # more useful and when are context managers more useful?

    # A. Context Managers allow easy ending of operation without specifying it to do so explicitly. Decorators
    # on the other hand wrap a function around with another function and applies the former to the latter, similar to a nesting.
    # Both have the same effect of running two functions at a time, however the former ensures that both functions run without error while the latter provides
    # cleaner syntax, hence it is called 'syntactic sugar.'

    # Use Cases:
    # Use Context Managers to ensure clean-up without explicitly telling the computer to do so.
    # Use Decorators to efficiently nest functions together.



#########################
if __name__ == '__main__':
    main()