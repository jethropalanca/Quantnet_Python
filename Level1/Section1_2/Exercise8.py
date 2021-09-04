'''
This program involves zipping and lists.
'''

def main():
    names = ['Michael', 'LeBron', 'Kobe', 'Kareem', 'Shaquille', 'Wilt', 'Larry', 'Magic', 'Julius', 'Bill']
    ages = [12, 13, 26, 18, 56, 85, 2, 69, 77, 14]

    namesWithAges = zip(names,ages)
    print(list(namesWithAges))

    lst = [name for name,age in zip(names,ages) if age >= 18]
    print(lst)

    # Q. Is Zip better than without Zip?
    # A. I think it would be more difficult without zip as we would need to use loops. Moreover, if we use loops, code will be longer and less efficient, so Zip is better and faster.


if __name__=='__main__':
    main()


