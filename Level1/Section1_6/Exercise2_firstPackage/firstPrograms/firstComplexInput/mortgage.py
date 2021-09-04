'''
Create a mortgage list and sort
'''

def mortgage(number_mortgages):

    import random
    print('Please enter how many mortgages you want to pull for your list:')

    random.seed(1000)
    mortgageList = [random.randint(100, 1000) for i in range(int(number_mortgages))]

    print('\n','Here is a list of your mortgages (in thousands):')
    print(mortgageList)
    return mortgageList
