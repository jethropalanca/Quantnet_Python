'''
This program is a rework of 1.2.7 (per Quantnet forum interaction with Karandhir), using set functionalities.
'''

def main():
    players = set(['Michael', 'LeBron', 'Kobe', 'Kareem', 'Shaquille', 'Wilt', 'Larry', 'Magic', 'Julius', 'Bill'])
    injured_players = set(['Kobe', 'Bill', 'Michael', 'Luke', 'Mark', 'David'])

    active_players = players.difference(injured_players)
    print(active_players)

    # Q. What is the benefit of using lists instead of sets
    # A. Sets are more efficient as they take advantage of set operations vs. lists which have to do things iteratively.


if __name__=='__main__':
    main()


