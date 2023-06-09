#1
"""
Use readData to read in the data and create DS
    This function takes in a file handle as parameter and reads in the data in friends.txt and loads the data to the global variable DS.

    The name of the data structure must be DS. It's structure is as follows.

    DS = [[Child1 name, age, gender, [Sibling1, Sibling2, …],  [Friend1, Friend2, …] ], [Child2 name, age, gender, [Sibling1, Sibling2, …],  [Friend1, Friend2, …] ], etc.]

    This global variable is used by other functions as needed.
"""
def readData(filehandle):
    #call global variable DS
    global DS
    DS = []
    with open(filehandle, 'r', encoding='utf-8') as file_in:
        for line in file_in:
            #strip to get rid of "/n"
            splitted_line = line.strip()
            #split to get rid of "|"
            splitted_line = splitted_line.split("|")
            #remove any remaining empty spaces in strings
            splitted_line=[element.strip() for element in splitted_line]
            #append DS as asked in Problem 1
            DS.append([splitted_line[0], splitted_line[1].split(", "), splitted_line[2].split(", ")])
        for element in DS:
          element[0] = element[0].split(', ')
    return(DS)
readData("friends.txt")


#2
"""
def printDetails:
    '''
    This function takes a child’s name as parameter and prints out
    the details nicely and appropriately as for example:

    Child Name: John Adam. He has 3 siblings and 3 friends.

    Siblings:
	Jacob, Dan and Sarah

    Friends:
	Joe, Emily and Susan
    '''
"""
def printDetails():
    for _ in range(len(DS)):
        #check if sibling is empty as in case of Tim Duke
        if DS[_][1][0] == "":
            #introduce each child, his/her sibling and friend number
            print('Child name:', DS[_][0][0] + "." + " This child has 0" + " sibling(s) and " + str(len((DS[_][2]))) + " friend(s).")
            print(" ")
            #print siblings for each child
            print("Siblings:")
            siblings=""
            for num in range(len(DS[_][1])):
                siblings += str((DS[_][1][num])) + ", "
            print(siblings[:-2] + "\n")
            #print friends for each child
            print("Friends:")
            friends=""
            for num in range(len(DS[_][2])):
                friends += str((DS[_][2][num])) + ", "
            print(friends[:-2] + "\n")
        else:
            #introduce each child, his/her sibling and friend number
            print('Child name:', DS[_][0][0] + "." + " This child has " + str(len((DS[_][1]))) + " sibling(s) and " + str(len((DS[_][2]))) + " friend(s).")
            print(" ")
            #print siblings for each child
            print("Siblings:")
            siblings=""
            for num in range(len(DS[_][1])):
                siblings += str((DS[_][1][num])) + ", "
            print(siblings[:-2] + "\n")
            #print friends for each child
            print("Friends:")
            friends=""
            for num in range(len(DS[_][2])):
                friends += str((DS[_][2][num])) + ", "
            print(friends[:-2] + "\n")
printDetails()


#3
"""
use lambda functions to:
  a) sort DS by age
  b) sort DS by the name of the first friend in the list
"""
#a
sorted(DS, key = lambda z : int(z[0][1]))
#b
#lower is added to compare between uppercase and lowercase names equally
sorted(DS, key = lambda z : (z[2][0]).lower())


#4
'''
    Use function findCommonFriends to print out the common friends for 
    a) 'Sara Adam' and 'John Adam'
    b) 'Stan Silva' and 'Dan Adam'  
    c) Write code that includes list comprehension to create the set of friend  names in the dataset that do not have the letter 'a' in it. Print out this set. You might consider doing this in 2 steps. First create a set of all friend names then use list comprehension.
'''
#a
def findCommonFriends(c1, c2):
    '''
    c1 and c2 are the names of children
    This function returns a set containing the friends in common
    between c1 and c2.
    '''
    #create a list of friends for c1
    for num in range(len(DS)):
      if c1 == DS[num][0][0]:
        friends_c1 = DS[num][2]
    #create a list of friends for c2
    for num in range(len(DS)):
      if c2 == DS[num][0][0]:
        friends_c2 = DS[num][2]
    #create a list of common friends
    common_friends = [x for x in friends_c1 if x in friends_c2]
    return(common_friends)
a = findCommonFriends("Sara Adam", "John Adam")
print(a)

#b
b = findCommonFriends('Stan Silva', 'Dan Adam')
print(b)

#c
#collect all possible names without repetition
all_names = set()
for num in range(len(DS)):
  i = 0
  while i < len(DS[num][2]):
    all_names.add(DS[num][2][i])
    i+=1
#print(all_names) #don't print it
#list comprehension to create names without a and A
names_no_a = set([name for name in all_names if "a" not in name and "A" not in name])
print(names_no_a)


#5
'''
    Use function findAllCommonFriends to write to a file output.txt
    details about the common friends for all pairs of
    children (without redundancy - i.e., details for a pair are
    written only once).
    
    Choose a suitable print format as for example:
    
    child 1 name, child 2 name: common friend names separated by comma.
    E.g.

    Sara Adam, John Adam: Emily
    
    If there are no common friends for a pair,
    it should print out
    child 1 name, child 2 name, No common friends
'''

def findAllCommonFriends():
    '''
    This function uses function commonFriend to iteratively
    compute the common friends for all pairs of children.

    This information is stored in a list called friends where
    each entry has 3 parts,

    [Child1 name, child2 name, a set of their common friend names]

    To illustrate:

    friends =
    [
    ['Sara Adam', 'John Adam', {'Emily'}],
    [...],
    etc.
    ]
    The function returns friends.
    '''
    children_pairs = []
    for x in range(len(DS)):
      for y in range(len(DS)):
        #eliminate cases where both x and y is the same child
        if x == y:
          pass
        else:
          children_pairs.append({DS[x][0][0], DS[y][0][0]})
    #eliminate duplicates
    no_duplicate_children = []
    #print(len(children_pairs))
    for i in children_pairs:
      if i not in no_duplicate_children:
        no_duplicate_children.append(i)
    #print(len(no_duplicate_children))   
    #print(no_duplicate_children)

    #convert children pairs from sets into lists
    big_list = []
    for s in no_duplicate_children:
      mini_list = []
      for element in s:
        mini_list.append(element)
      big_list.append(mini_list)
    #print(big_list)   
    #with open('out2.txt','a') as file_out:
    
    #use findCommonFriends function
    friends = []
    for num in range(len(big_list)):
      friend = findCommonFriends(big_list[num][0], big_list[num][1])
      friends.append([big_list[num][0], big_list[num][1], set(friend)])
    return friends
    #print(friends)
   
friends = findAllCommonFriends()
#write output.txt file
with open('output.txt','a') as file_out:
  for num in range(len(friends)):
    if len(friends[num][2]) == 0:
      file_out.write('\n' + friends[num][0] + ', ' + friends[num][1] + ': ' + ' No common friends' + '\n')
    elif len(friends[num][2]) == 1:
      file_out.write('\n' + friends[num][0] + ', ' + friends[num][1] + ': ' + str(friends[num][2])[2:-2] + '\n')
    elif len(friends[num][2]) == 2:
      file_out.write('\n' + friends[num][0] + ', ' + friends[num][1] + ': ' + str(friends[num][2])[2:-2].replace("'","") + '\n')

      
#6
'''
    Use function sortByNumFriends to print the name of the child with
    the most friends. If there are ties print names of all children
    that qualify.

'''

def sortByNumFriends():
    '''
    This function returns DS2 which is identical in
    structure to DS except that it's records are sorted in increasing
    order by number of friends.
    '''
    sorted_DS = sorted(DS, key = lambda z : len(z[2]))
    return(sorted_DS)
sorted_DS = sortByNumFriends()
#counter to calculate maximum number of friends, l
l = 0
for _ in range(len(sorted_DS)):
  if l < len(sorted_DS[_][2]):
    l = len(sorted_DS[_][2])
#print children with max amount of friends based on l
#print to make space for better output visualization
print('')
for _ in range(len(sorted_DS)):
  if l == len(sorted_DS[_][2]):
    print(sorted_DS[_][0][0])


#main function
def main():
    if __name__ == "__main__":
        print ("This is the sequence of steps to reach program goal:\n")
        #initialize()
        #open a file handle in to read
        readData("friends.txt")
        printDetails()
        friends = findAllCommonFriends()
        with open('output.txt','a') as file_out:
            for num in range(len(friends)):
              if len(friends[num][2]) == 0:
                file_out.write('\n' + friends[num][0] + ', ' + friends[num][1] + ': ' + ' No common friends' + '\n')
              elif len(friends[num][2]) == 1:
                file_out.write('\n' + friends[num][0] + ', ' + friends[num][1] + ': ' + str(friends[num][2])[2:-2] + '\n')
              elif len(friends[num][2]) == 2:
                file_out.write('\n' + friends[num][0] + ', ' + friends[num][1] + ': ' + str(friends[num][2])[2:-2].replace("'","") + '\n')
        sortByNumFriends()
        sorted_DS = sortByNumFriends()
        #counter to calculate maximum number of friends, l
        l = 0
        for _ in range(len(sorted_DS)):
          if l < len(sorted_DS[_][2]):
            l = len(sorted_DS[_][2])
        #print children with max amount of friends based on l
        #print to make space for better output visualization
        print('')
        for _ in range(len(sorted_DS)):
          if l == len(sorted_DS[_][2]):
            print(sorted_DS[_][0][0])