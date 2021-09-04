'''
This function takes and displays all passed-in keyword arguments, no matter what the key is.
'''

def myFunction(name, age, **kwargs):
    print('\n', name, age)
    for key, value in kwargs.items():
        print(key+str(':'),value)


def main():
    myFunction('Ned', 29, state = 'New York', height = 69, weight = 150)
    myFunction('Julius', 23, state = 'Metro Manila', height = 64, hairColor = 'Brown')
    myFunction('Crawford', 25, state = 'New York', height = 75, weight = 138)
    myFunction('Pawan', 28, state = 'New Gujarat', weight = 150, height = 62)
    myFunction('Nami', 20, state = 'Calamity', handed = 'Left Handed')


if __name__=='__main__':
    main()

