'''
This program applies string manipulation on the text ' The python course is the best course that I have ever taken.
'''


def main():
    # Initialize...
    print('Initialize... (String Functionality with Naive Strings Practice)')
    s = ' The Python course is the best course that I have ever taken. '

    print('\n(I) Part 1.')

    # 1 Display the length of the string.
    print('# 1 Display the length of the string.')
    print(len(s))

    # 2 Find the index of the first 'o' in the string.
    print('\n# 2 Find the index of the first \'o\' in the string.')
    print(s.index('o'))

    # 3 Trim off the leading spaces only.
    print('\n# 3 Trim off the leading spaces only.')
    print(s.lstrip())

    # 4 Trim off the trailing spaces only.
    print('\n# 4 Trim off the trailing spaces only.')
    print(s.rstrip())

    # 5 Trim off both the leading and trailing spaces (use this trimmed string for all the remaining
    # parts below).
    print('\n# 5 Trim off both the leading and trailing spaces (use this trimmed string for all the remaining parts below.).')
    print(s.strip())

    print('(II) Part 2.')
    s2 = s.strip() # No more trailing / leading spaces.

    # 6 Fully capitalize the string.
    print('\n# 6 Fully capitalize the string.')
    print(s2.upper())

    # 7 Fully lowercase the string.
    print('\n# 7 Fully lowercase the string.')
    print(s2.lower())

    # 8 Display the number of occurrence of the letter ‘d’ and of the word ‘the’.
    print('\n# 8 Display the number of occurrence of the letter ‘d’ and of the word ‘the’.')
    print('Number of occurence of the letter \'d\':',s2.count('d'),'.')
    print('Number of occurence of the word \'the\':',s2.count('the'),'.')

    # 9 Display the first 15 characters of the string.
    print('\n# 9 Display the first 15 characters of the string.')
    print('The first ', len(s2[:15]), ' characters:')
    print(s2[:15])

    # 10 Display the last 10 characters of the string.
    print('\n# 10 Display the last 10 characters of the string.')
    print('The last ', len(s2[-10:]), ' characters:')
    print(s2[-10:])

    # 11 Display characters 5-23 of the string.
    print('\n# 11 Display characters 5-23 of the string.')
    print(s2[5:23])

    # 12 Find the index of the first occurrence of the word ‘course’.
    print('\n# 12 Find the index of the first occurrence of the word ‘course’.')
    print(s2.find('course'))

    # 13 Find the index of the second occurrence of the word ‘course’.
    print('\n# 13 Find the index of the second occurrence of the word ‘course’.')
    loc = s2.find('course')
    print(s2.find('course', loc+1))

    # 14 Find the index of the second to last occurrence of the letter ‘t’, between the 7th and 33rd
    # characters in the string.
    print('\n# 14 Find the index of the second to last occurrence of the letter ‘t’, between the 7th and 33rd characters in the string.')
    loc = s2.rfind('t', 7, 33)
    print(s2.rfind('t', 7, loc))

    # 15 Replace the period (.) with an exclamation point (!).
    print('\n# 15 Replace the period (.) with an exclamation point (!).')
    print(s2.replace('.', '!'))

    # 16 Replace all occurrences of the word ‘course’ with ‘class’.
    print('\n# 16 Replace all occurrences of the word ‘course’ with ‘class’.')
    print(s2.replace('course', 'class'))




#########################
if __name__ == '__main__':
    main()
