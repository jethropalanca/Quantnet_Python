'''
This program creates a mode function.
'''

def freqMap(values):
    map={}
    for v in values:
            if not map.get(v):
                map[v] = 1
            else:
                map[v]=map[v]+1
    return map

def mode(values):

    dictFreqmap = freqMap(values)

    # Initial Code: Does not account for Multi-modal
    # sorted_dictFreqmap = dict(sorted(dictFreqmap.items(), key = itemgetter(1), reverse = True))

    # Final Code: Accounts for multi-modal
    maxval = max(dictFreqmap.values())
    dictFreqmap_Final = [(a, b) for a, b in dictFreqmap.items() if b == maxval]

    return dictFreqmap_Final


def main():
    print('\nFrequency of Each Entry (data dict):', freqMap([2,3,2,2,2,5,10,4,6,7,1,2,3,4,7,7,8,9,10,11,12,13,11,1,2,3,4,11,6,7,8,9,11,0]))
    print('Mode of List:', mode([2,3,2,2,2,5,10,4,6,7,1,2,3,4,7,7,8,9,10,11,12,13,11,1,2,3,4,11,6,7,8,3,9,3,11,0,3]))

if __name__=='__main__':
    main()


