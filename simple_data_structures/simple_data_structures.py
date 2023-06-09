'''

Working with tuples, dicts, arrays, creating somewhat complex data
structures from data in files.

'''
'''
Problem 1: Write a function readMatrix() that reads integer data from the file "matrixdata.txt"
into an array in 'row dominant' format. Below is an example to illustrate
row dominant format.
The function should return the array.

    [[4, 6, 9],
    [6, 8, 10],
    [14, 13, 6],
    [11, 16, 2]]

'''

def readMatrix():
    #read matrixdata.txt file
    with open('matrixdata.txt', 'r', encoding='utf-8') as file_in:
        row_matrix = []
        for line in file_in:
            #split based on ,
            splitted_line = line.split(", ")
            #convert to integers
            splitted_line = [int(element) for element in splitted_line]
            row_matrix.append(splitted_line)
    return(row_matrix)
#check function and see output
readMatrix()



'''
Problem 2: Write a function convert() which takes in a two dimensional matrix
of integers and returns a transformed matrix.  The transformation logic is as follows.
If the integer is odd you replace it with the corresponding uppercase alphabet
eg. 1 -> A, 9 -> I etc.  If it is an even integer replace with the corresponding
lower case alphabet.  e.g., 2 -> b and 4 -> d.

So for example:

    [[4, 6, 9],
    [6, 8, 10],
    [14, 13, 6],
    [11, 16, 2]]


is transformed into:

    [['d', 'f', 'I'],
    ['f', 'h', 'j'],
    ['n', 'M', 'f'],
    ['K', 'p', 'b']]

'''

def convert(matrix):
    #copy to change matrix
    import copy
    copied_matrix = copy.deepcopy(matrix)
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            #add condition for even integers
            if matrix[row][column]%2 == 0:
                #64 is required to get English alphabet letters
                copied_matrix[row][column] = chr( matrix[row][column]+64).lower()
            #add condition for odd integers
            else:
                copied_matrix[row][column] = chr( matrix[row][column]+64)
    return(copied_matrix)
#check function and see output
convert(readMatrix())


'''
Problem 3: Read in data from the file "teachers.txt" and create the following two
dictionaries.

Problem 3a
# keys are course names and values are a dictionary of course information (classes, hours and fee)
course_offerings = {'bash': {'classes': 10, 'hours': 2, 'fee': 500.50},
                    'PHP': {'classes': 30, 'hours': 3, 'fee': 1500.0},

                    etc.
                    
                    }

Problem 3b
# keys are teacher initials and values are courses the teacher teaches
teachers = {'MJ': ('bash', 'PHP', 'java'),
            'AS': ('sql', 'PHP', 'java'),

            etc.
            
            }

'''
#3a
with open("teachers.txt", 'r', encoding='utf-8') as file_in:
    course_offerings = {}
    for line in file_in:
        #get rid of teachers information (right side of |)
        splitted_line = line.split(" | ")[0].split(", ")
        #properly split remaining lists
        splitted_line = [element.split(" = ") for element in splitted_line]
        splitted_line[0][0] = splitted_line[0][0].split(': ')
        #fill course offerings with information
        course_offerings[splitted_line[0][0][0]] = {splitted_line[0][0][1]:splitted_line[0][1], splitted_line[1][0]:splitted_line[1][1], splitted_line[2][0]:splitted_line[2][1]}
    course_offerings

#3b
with open("teachers.txt", 'r', encoding='utf-8') as file_in:
    teachers = {}
    teacher_courses = []
    for line in file_in:
        #split based on |
        splitted_line = line.strip().split(" | ")
        #continue split to get courses from left side of | and teachers from right side of |
        teacher_courses.append([splitted_line[0].split(": ")[0], splitted_line[1].split(", ")])
        for num in range(len(teacher_courses)):
            for teacher in teacher_courses[num][1]:
                for num2 in range(len(teacher_courses)):
                    if teacher in teacher_courses[num2][1]:
                        #setdefault allows to create multiple dictionary values within the list
                        random = teachers.setdefault(teacher, [])
                        random.append(teacher_courses[num][0])
    #convert dictionary values to tuples
    for key in teachers:
        teachers[key] = tuple(set(teachers[key]))
    #check created dictionary
    teachers





