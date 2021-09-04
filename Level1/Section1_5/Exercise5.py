'''
This program creates a simple dictionary that has country name as the key and population as the value, and applies several dictionary functionalities.
'''

def main():
    # Data is from Worldometer, for 2021.
    dictCountry = {'China': 1439323776, 'India': 1380004385, 'United States': 331002651, 'Indonesia': 273523615, 'Pakistan': 220892340, 'Brazil': 212559417, 'Nigeria': 206139589,
                   'Bangladesh': 164689383, 'Russia': 145934462, 'Mexico': 128932753}
    countryNames = list(dictCountry.keys())


    # Prompt user for country.
    country = ''
    while country != '0':
        print('\n',countryNames)
        country = input('Please select a country from the list above to get its population (0 to stop):')
        if country != '0':
            value = ''
            if dictCountry.get(country) == None:
                try:
                    value = int(input('Population is unknown, please enter the population of that country:')) # Update Dict
                    dictCountry[country] = value
                except:
                    print('Please enter a number')
            else:
                print(country, dictCountry[country])
        else:
            break

    # Display Final Dictionary
    for country in dictCountry:
        print(country, 'has population ', dictCountry[country])

    # Sorting by Country
    sorted_dictCountry = dict(sorted(dictCountry.items()))
    print('\nAfter Sorting by Country:', sorted_dictCountry)

    # Sorting by Population, Largest First
    from operator import itemgetter

    sorted_dictCountry2 = dict(sorted(dictCountry.items(), key = itemgetter(1), reverse = True))
    print('After Sorting by Population:',sorted_dictCountry2)

    # Dict Comprehension to create a sub-dictionary with countries of population greater than 1 billion.
    dictCountry1B = {country:population for country, population in dictCountry.items() if population > 1000000000}
    print('SubDictionary of Countries with population GREATER than 1 Billion', dictCountry1B)

if __name__=='__main__':
    main()


