"""
Problem 1

Write a function oneVowel that takes in a string as argument.
It returns True if the string has only 1 vowel which occurs only once.
The function returns False in all other cases. The function ignores
case differences.

E.g.  	oneVowel('syndrome') 	returns False.

    	oneVowel ('fad') 		returns True.
    	
        oneVowel ('paragraph') 	returns False.
        oneVowel ('bxx') returns False

'''


def oneVowel:


'''
Problem 2


Write functions that take a string as argument.
The function identifies the leftmost character that occurs the MOST
number of times in the string (can be non consecutive occurrences).
The function returns a list containing this character and the position
of its leftmost occurrence.

'abracadabra' returns ['a', 0]

'bracradabrra' returns ['r', 1]

Test your functions well. For example:

If multiple characters occur the MOST number of times then
return the one that occurs earliest in the string.


e.g. in 'baseball' both b and l occur twice.  But the first b occurs before the
first l and so return b with position 0.

Note: Again your function should be case insensitive in its counting.

e.g. 'fAbddaBeeab' returns : The count for a (or A) is 3 and you may
return either [a, 1]  or [A, 1]

Solve this problem with 3 different functions. Each function takes in a single
argument representing the input string.  Note that below I am specifying the name
of each function that you need to submit. Please follow this naming scheme.


'''

def answer_with_while:

    '''
    use a single loop at it should be a while loop
    do not nest other loops inside it

    (do not use while True which is
    reserved for problem (c).
    '''

def  answer_with_for:
    '''
    use a single for loop.
    do not nest other loops inside it

    '''

def answer_with_while_true:
    '''
    use a single while True loop.
    do not nest other loops inside it

    '''


  
'''
Problem 3

Write a function listCompare that takes in two lists as arguments.
It then returns a new list containing only those elements of
list 1 (first argument of function) that
are smaller than ALL elements of list 2 (2nd argument).

Also when different boundary cases (e.g. empty list/s) arise
return 'Problem in your input lists'

E.g. given:

L1 = ['5', '27', '%', 'x', '33']
L2 = ['3', 'mat', '10', '22']

listCompare(L1, L2) should return ['%']

whereas listCompare(L2, L1) should return []

Similarly,

L1 = ['7', ' ', '18', 'ate' ,'33']
L2 = ['ate', '15']

listCompare(L1, L2) should return [' ']

whereas listCompare(L2, L1) should return []

listCompare([],[]) should return 'Problem in your input lists'



def listCompare:
    
"""


#1
def oneVowel(string):
  vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'w'] 
  i = 0
  #make sure that function takes only strings
  if type(string) is str:
    #make input case insensitive
    for letter in string.lower():
      if letter in vowels:
        i += 1
    if i == 1:
      return True
    else:
      return False
  #message in case if other data structures inputed
  else:
    print("Please input string!")

#2
#a
def answer_with_while(string):
  #make sure that function takes only strings
  if type(string) is str:
    #make input case insensitive
    string = string.lower()
    i = 0
    n = 0
    while i < len(string):
      if string.count(string[i]) > n:
        list = []
        list.extend([string[i], i])
        n = string.count(string[i])
      i += 1
    return(list)
  #message in case if other data structures inputed
  else:
    print("Please input string!")
#b
def answer_with_for(string):
  #make sure that function takes only strings
  if type(string) is str:
    #make input case insensitive
    string = string.lower()
    n = 0
    for letter in string:
      if string.count(letter) > n:
        list = []
        list.extend([letter, string.index(letter)])
        n = string.count(letter)
    return(list)
   #message in case if other data structures inputed
  else:
    print("Please input string!")
#c
def answer_with_while_true(string):
  #make sure that function takes only strings
  if type(string) is str:
    #make input case insensitive
    string = string.lower()
    i = 0
    n = 0
    while True:
      if i == len(string):
        break
      elif string.count(string[i]) > n:
        list = []
        list.extend([string[i], i])
        n = string.count(string[i])
      i += 1
    return(list)
  #message in case if other data structures inputed
  else:
    print("Please input string!")

#3 
def listCompare(list1, list2):
  try:
    #check that both inputs are list
    if type(list1) is list and type(list2) is list:
      new_list = []
      #identify the smallest element of list2
      list2_min = min(list2)
      for element in list1:
        if element < list2_min:
          new_list.append(element)
      return(new_list)
    #message in case if inputs are not lists
    else:
      print("Please input lists!")
  except:
    print('Problem in your input lists')
