path_to_file = "books/frenkenstein.txt"

def getWordcount(text):
    wordlist = text.split()
    return len(wordlist)

def countLetters(text):
    text = text.lower()

    ret = {}

    for char in text:
        if not char.isalpha():
            continue
        if char in ret.keys():
            ret[char] += 1
        else:
            ret[char] = 1
    
    return ret

def sortLetters(letterDic):
    
    letterList = []
    
    for key in letterDic:
        letterList.append([letterDic[key],key])

    letterList.sort()
    letterList.reverse()
    return letterList

with open(path_to_file) as f:
    file_contents = f.read()

#print(file_contents)
wordCount = getWordcount(file_contents)
letterCount = countLetters(file_contents)
sortedCount = sortLetters(letterCount)
print(f"--- Begin report of {path_to_file} ---")

print(f"{wordCount} words found in the document")
for row in sortedCount:
    print(f"The '{row[1]}' character was found {row[0]} times")