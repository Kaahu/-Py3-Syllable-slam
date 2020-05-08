# Syllable Slam
# Takes a word or list of words and counts the syllables for each word.
# Uses two approaches to output the syllable count:
#    - Use a dictionary, if the word is in the dictionary and output the
#      syllable count
#    - If word is not in the dictionary, calculate the syllable count via
#      algorithm. 
#
# Authors: Mickey Treadwell, Josef Bode, Ben McCarthy, Josh Signal

import re, fileinput

#_______GLOBAL VARIABLES______

sylls = 0
dictionary = {}


#__________EXCEPTIONS_________

def exceptions(word):
    global sylls

    exceptions_le = ['whole', 'mobile', 'pole', 'male', 'female', 'hale',
                     'pale', 'tale', 'sale', 'aisle', 'whale', 'while']
    exceptions_les = ['wholes', 'mobiles', 'poles', 'males', 'females',
                      'hales', 'pales', 'tales', 'sales', 'aisles',
                      'whales', 'whiles']
    
    # Silent 'e'
    if len(word) > 1 and word[-1] == 'e':
        sylls -= 1

    # Ends with 'le' (e.g. scribble)
    if (word[-2:]) == 'le' and word not in exceptions_le:
        sylls +=1

    # Ends with 'les'
    if (word[-3:]) == 'les' and word not in exceptions_les:
        sylls +=1

    # Unusual, annual
    if 'ual' in word:
        sylls +=1

    # Schism, Rhythm
    if len(word) > 1 and word[-1] == 'm':
        if word[-2:] == 'sm':
            sylls +=1
        elif word[-3:] == 'thm':
            sylls +=1

    # 'ed' for past tense verbs
    if len(word) > 2 and word[-2:] == "ed":
        sylls -=1
        if (word[-3] == 't' or word[-3] =='d' or word[-3] =='i'):
            sylls +=1

    # 'es' 
    if len(word) > 2 and word[-2:] == "es":
        sylls -=1
        if (word[-3] == 't' or word[-3] =='d' or word[-3] =='i' or word[-3] =='s'):
            sylls +=1

    # starts with 'mc'
    if word[:2] == 'mc':
        sylls += 1

    # does 'o' come after 'i'
    # (e.g. physio, scenario)
    if 'io' in word or 'ia' in word or 'uie' in word:
        if 'tio' in word:
            pass
        else:
            sylls += 1

    # dealing with 'oic'
    if 'oic' in word:
        sylls += 1

    # Just in case
    if sylls <= 0:
        sylls = 1

#__________ALGORITHM APPROACH_________

def checkalgorithm(word):
    global sylls
    
    splitword = re.split('b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|z', word)

    while '' in splitword:
        splitword.remove('')

    sylls = len(splitword)
    exceptions(word)

    print(sylls)

#__________DICTIONARY APPROACH_________

# Support method for processing lines into dictionary
def hasdigit(inputstring):
    return any(char.isdigit() for char in inputstring)

# Extract number of syllables from the CMU dictionary file
def processline(line):
    syll = 0
    dictentry = ['','']
    dictentry[0] = line[0]
    for i in line[1:]:
        if hasdigit(i):
            syll += 1
            dictentry[1] = syll
    return dictentry

# Fill dictionary with processd contents of CMU dictionary file
def filldictionary():
    global dictionary
    
    f = open("cmudict.txt", 'r')
    contents = f.readlines()
    for line in contents:
        line = str(line).lower().split()
        dictentry = processline(line)
        dictionary[dictentry[0]] = dictentry[1]
        f.close()

def checkdictionary(inputword):
    if word in dictionary:
        print(dictionary[word])
    else:
        return "fail"
        
#__________EXECUTION_________

filldictionary()

for line in fileinput.input():
    word = line.lower().rstrip()
    if word ==  '':
        break
    if checkdictionary(word) is "fail":
        checkalgorithm(word)

    
    
