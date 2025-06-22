#cli interface
from password_strength import password_check
from custom_wordlist import wordlist_generator 
from save_file import save_as_txt
import argparse
#defining args
def main():
    parser=argparse.ArgumentParser(Description="Password Strength Analysis")
    parser.add_argument("-p","--password",help="password analysis")
    parser.add_argument("-n","--name",help="user name")
    parser.add_argument("-d","--dob",help="date of birth")
    parser.add_argument("-pet","--pet",help="name of pet")
    parser.add_argument("-e","--extra",nargs="*",help="extra words")
    parser.add_argument("-export",action='store_true',help="export genrated keywords")
    args=parser.parse_args()
    if args.password:
        password_check(args.password)
    if args.name or args.dob or args.pet:
        wordlist=wordlist_generator(args.name or "" ,args.dob or "", args.pet or "" , args.extra or [])
        for word in wordlist:
            print(wordlist)
        if args.export:
            save_as_txt(wordlist)
if __name__ == "__ main __":
    main()


