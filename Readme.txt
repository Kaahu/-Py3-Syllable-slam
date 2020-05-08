SyllableSlam.py

________KIA ORA!___________________________________________________________

Syllable Slam is a simple Python program to count the number of syllables 
in a given word, or file of words.

The program first checks the given word/words against an English language
dictionary containing the corresponding syllable count for each word.

If the given word is not included in the dictionary, the word is broken
down into vowel groups which are counted, then various features of the word
are examined to add/subtract syllables from the total count.

Note: the program includes a modified copy of the CMU Dictionary 
("cmudict.txt") which must be in the same directory when "syllableslam.py" 
is run. This is a comprehensive dictionary of words stored with their 
associated number of syllables.

________HOW TO RUN_________________________________________________________

Navigate to the program directory in terminal and ensure that "cmudict.txt"
is in the same directory.

The user has two options for running the program: either give no arguments 
or give the program a text file that contains a list of words, with a single 
word per line.

NO ARGUMENTS:

e.g. terminal input: $ python3 syllableslam.py 
When no arguments are given, the program will accept words from standard 
input and will count the syllables. Press [enter] without any input to exit 
program.

GIVE TEXT FILE:
e.g. terminal input: $ python3 syllableslam.py test.txt
This will make the program read a list of words from the given file and 
counts the syllables for each word.

________AUTHORS__________________________________________________________

Benjamin McCarthy
Josef Bode
Mickey Treadwell
Josh Signal
