'''
This program creates a set of mortgage terms.
'''

def main():

# Create a set of Mortgage terms
    setMortgage = set([10, 15, 30])
    print(setMortgage)

# Add a 5-year term to the set
    setMortgage.add(5)
    print(setMortgage)

# Remove 15-year term to the set
    setMortgage.remove(15)
    print(setMortgage)

# Remove 45-year term
    try:
        setMortgage.remove(45)
    except:
        print('\nAn error occurs if you remove a non-existent item from the set. To prevent that, we use set.discard instead of set.remove')
        setMortgage.discard(45)
    print(setMortgage)

# Q. What happens when you remove a 45-year term from the set? How do you prevent that?
# A. An error occurs if you remove a non-existent item from the set. To prevent that, we use set.discard instead of set.remove

if __name__=='__main__':
    main()


