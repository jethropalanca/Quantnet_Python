'''
This program creates two sets and does some set operations.
'''

def main():

# Popular Baby Boy Names Data taken from US SSS and UK Office for National Statistics (2019)
    setUS = set(['Liam', 'Noah', 'Oliver', 'William', 'Elijah', 'James', 'Benjamin', 'Lucas', 'Mason', 'Ethan', 'Alexander', 'Henry', 'Jacob', 'Michael', 'Daniel', 'Logan', 'Jackson', 'Sebastian', 'Jack', 'Aiden'])
    setUK = set(['Oliver', 'George', 'Noah', 'Arthur', 'Harry', 'Leo', 'Muhammad', 'Jack', 'Charlie', 'Oscar', 'Jacob', 'Henry', 'Thomas', 'Freddie', 'Alfie', 'Theo', 'William', 'Theodore', 'Archie', 'Joshua'])

    print('Top 20 US Popular Baby Names:', setUS)
    print('Top 20 UK Popular Baby Names:', setUK)

# Find the first names that appear in both sets:
    print('\nFirst Names that appear in BOTH sets:', setUS.intersection(setUK))

# Find the first names that appear in the United States set, but not Britain:
    print('First Names that appear in the US set BUT NOT in UK:', setUS.difference(setUK))

# Find the first names that appear in the Britain set, but not United States:
    print('First Names that appear in the UK set BUT NOT in US:', setUK.difference(setUS))

# Set comprehension to create a subset of names that have more than five letters:
    print('\nSubset of names in both sets that have more than five letters:', {i for i in setUS.union(setUK) if len(i) > 5})

if __name__=='__main__':
    main()


