wordlist1 = input('Enter name of base wordlist (ex: adjectives.txt): ')
wordlist2 = input('Enter name of second wordlist: ')

combined_wordlist = []

with open(wordlist1, mode='r') as file1:
    for item in file1:
        with open(wordlist2, mode='r') as file2:
            for word in file2:
                combined_wordlist.append(f'{item.strip()}{word.strip()}')

with open('combined_wordlist.txt', mode='a') as file3:
    for item in combined_wordlist:
        file3.write(f'{item}\n')






