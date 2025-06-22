#wordlist generator
import itertools
from password_strength import password_check
def wordlist_generator(name,dob,pet,extra=[]):
    words=[name.lower(),dob.lower(),pet.lower()]+ [word.lower() for word in extra]
    leetspeak={'a':'@','s':'$','g':'&'}
#transforming the alphabets
    def leet_transform(word):
         return''.join([leetspeak.get(c,c) for c in word])
    
#adding all the types of words
    wordlist=set()
    for word in words:
           wordlist.add(word)
           wordlist.add(word.capitalize())
           wordlist.add(leet_transform(word))
           for year in ['2023','2022','2002']:
                wordlist.add(f"{word}{year}")
                wordlist.add(f"{year}{word}")
    return sorted(wordlist)

