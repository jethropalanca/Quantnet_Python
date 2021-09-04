'''
This program creates two lists and manipulates them to create a third one called active_players.
'''

def main():
    players = ['Michael', 'LeBron', 'Kobe', 'Kareem', 'Shaquille', 'Wilt', 'Larry', 'Magic', 'Julius', 'Bill']
    injured_players = ['Kobe', 'Bill', 'Michael', 'Luke', 'Mark', 'David']

    active_players = [player for player in players if player not in injured_players]
    print(active_players)

if __name__=='__main__':
    main()


