#wordlist generator
import itertools
from password_strength import password_check
def wordlist_generator(name,dob,pet,extra=[]):
    words=[name.lower(),dob.lower(),pet.lower()]+ [word.lower() for word in extra]
    leetspeak={'a': ['a', '@', '4'],
        'b': ['b', '8', '6'],
        'c': ['c', '(', '<', '[', '{', '¢'],
        'd': ['d'],
        'e': ['e', '3'],
        'f': ['f'],
        'g': ['g', '9', '&'],
        'h': ['h', '#'],
        'i': ['i', '1', '!', '|'],
        'j': ['j'],
        'k': ['k'],
        'l': ['l', '1', '|', '£'],
        'm': ['m'],
        'n': ['n'],
        'o': ['o', '0'],
        'p': ['p', '9'],
        'q': ['q'],
        'r': ['r', '2'],
        's': ['s', '$', '5'],
        't': ['t', '7', '+'],
        'u': ['u', 'v'],
        'v': ['v', '/'],
        'w': ['w', '//'],
        'x': ['x', '%'],
        'y': ['y'],
        'z': ['z', '2']
    }
#transforming the alphabets
    def leet_transform(word):
         result = []
         for c in word:
             char_options = leetspeak.get(c.lower(), [c])
             result.append(char_options[1] if len(char_options) > 1 else char_options[0])
         return ''.join(result)
    
#adding all the types of words
    wordlist=set()
    for word in words:
           wordlist.add(word)
           wordlist.add(word.capitalize())
           wordlist.add(word.upper())
           wordlist.add(leet_transform(word))
           for year in ['2023','2022','2002']:
                wordlist.add(f"{word}{year}")
                wordlist.add(f"{year}{word}")
    return sorted(wordlist)

