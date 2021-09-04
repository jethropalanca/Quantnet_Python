'''
This function returns the Fibonacci sequence as a list (iterative/recursive).
'''

########### Iterative Version ###########
def fibonacci(N):
    list = [0]
    a = 0
    b = 1

    for c in range(N-1):
        a,b = b,a+b
        list.append(a)

    return list

########### Recursive Version ###########
def fibonacciRecursive(N):

    # Initial Conditions
    if N == 1:
        return [0]
    elif N == 2:
        return [0, 1]

    # Recursion Portion (Lalithnarayan)
    else:
        value = fibonacciRecursive(N - 1)
        value.append(sum(value[:-3:-1]))
        return value

def main():
    answer1 = fibonacci(25)
    answer2 = fibonacciRecursive(25)

    print('\nEntered 25 to the functions:')
    print(fibonacci(25))
    print(fibonacciRecursive(25))
    print(answer1 == answer2)


if __name__=='__main__':
    main()


