'''
This function returns the Fibonacci sequence as a list (recursive).
'''


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