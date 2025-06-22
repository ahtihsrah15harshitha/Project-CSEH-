#export to txt file
def save_as_txt(wordlist,filename="Custom wordlist"):
    with open(filename,'w') as f:
        for w in wordlist:
            f.write(f"{w}\n")
    print(f"file has been created as{filename}")