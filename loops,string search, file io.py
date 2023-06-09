"""

1. Write a program that when given string of alphabetic characters and a positive 
integer adjusts the string as illustrated below.
Input: ‘sssttRRRRRRnnnnnvqss’. Integer 3
Output: ‘ssstttRRRnnnvvvqqqsss’
In other words, the program outputs a string where each character repeats 3 times.
Write this program so that you accept input string and positive integer from the user.

2. Write and test a Python program that reads a list of words one by one from a given text file
(words.txt). The program should print out at the terminal, words whose characters are ordered 
in decreasing alphabetic sequence. That is the position of each character in the words should be 
in reverse alphabetic sequence.
e.g. tonne should be printed since its letters are in reverse order. Note that sequential 
occurrences of the same character is also fine. Spot should not be printed out. Your 
code must ignore case. Thus, ‘S’ is assumed to be equal to ‘s’.
The program should also print out the longest word(s) in the given text file that is of this 
type. 

3. Write and test a Python program that reads a list of words one by one from a given 
text file and print those words that have at least 3 of the distinct consonants in them.
Note that repetitions of a consonant in a word counts as a single consonant.
Use the same text file words.txt given to you for problems 2.

"""


#1
#getting string input
string = input('input a string: ')
#checking whether each next letter in a string differs from the previous letter in a string 
unique_char = ''
unique_char += string[0]
i = 1
while i < len(string):
  if string[i] != string[i-1]:
    unique_char += string[i]  
  i += 1

#getting positive integer input
while True:
  integer = input('input a positive integer: ')
  try:
    integer = int(integer)
    if integer < 1:
      print("Sorry, input must be a positive integer")
      continue
    break
  except ValueError:
    print("That's not an integer, input a positive integer")

#print based on input string and positive integer from the user
repeated_string = ''
for char in unique_char:
  repeated_string +=char*integer
print(repeated_string)

#2 
from string import ascii_lowercase
with open("words.txt", 'r', encoding='utf-8') as file:
  #getting char order
  for line in file:
    char_order = []
    for letter in line:
      try:
        char_order.append(ascii_lowercase.index(letter.lower()) + 1)
      except:
        continue
    #checking whether the order is reverse
    flag = 0
    i = 1
    while i < len(char_order):
        if(char_order[i] > char_order[i - 1]):
            flag = 1
        i += 1
    if (not flag) :
      #printing words with reverse order
      print (line)

#3 
consonants = "bcdfghjklmnpqrstvwxyz"
with open("words.txt", 'r', encoding='utf-8') as file:
  for line in file:
    #account for for consonant repetitions in a word 
    consonant_count = set()
    for letter in line:
        letter = letter.lower()
        print(letter)
        if letter in consonants:
            consonant_count.add(letter)
    #prints letters with at least 3 distinct consonants
    if len(consonant_count) > 2:
      print(line)