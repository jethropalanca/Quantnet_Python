'''
This function takes and displays, name, age, and state/height/weight if entered as input in **kwargs.
'''

def myFunction(name, age, **kwargs):
    print('\n',name, age)
    print(kwargs.get('state'))
    print(kwargs.get('height'))
    print(kwargs.get('weight'))
    print(kwargs.get('hairColor'))


def main():
    myFunction('Ned', 29, state = 'New York', height = 69, weight = 150)
    myFunction('Julius', 23, state = 'Metro Manila', height = 64, hairColor = 'Brown')
    myFunction('Crawford', 25, state = 'New York', height = 75, weight = 138)
    myFunction('Pawan', 28, state = 'New Gujarat', weight = 150, height = 62) # Lesson: Order is based on function's original set-up, not in how you input your variables
    myFunction('Nami', 20, state = 'Calamity')


if __name__=='__main__':
    main()


