'''
This function returns the Fibonacci sequence as a list (iterative).
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
