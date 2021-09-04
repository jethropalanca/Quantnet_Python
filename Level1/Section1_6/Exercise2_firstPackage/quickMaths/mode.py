'''
Putting it all together: this program creates a mode function.
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