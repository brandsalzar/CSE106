# #1 write and adding program that does the following:
# x = input("Enter two or more to sum separated by spaces:")
# y = 0

# stringList = x.split()

# if len(stringList) >= 2:
#     sum = 0
#     for i in stringList:
#         y = int(i)
#         sum = sum + y
#     print(sum)
# else:
#     print("error, need more than one number")

# #2) Write a punishment automation program in Python that does the following (15 points):
# sent = input("Enter a sentence:")
# #
# print("How many times should the sentence be writen as punishment:")
# repeats = int(input())

# f = open("CompletePunishment.txt", "w")
# for x in range(repeats):
#        f.write(sent + "\n")
# f.close()

# #3) Write a word count program in Python that does the following (25 points):
# #   a. Prompt the user to enter a word
# #   b. Parse PythonSummary.txt and count the number of times the word occurs in the file
# #   c. Tell the user how many times the word occurs
# #   d. Note: It should find the word regardless of case (upper or lower) or punctuation
# #   e. Example:
# #       i. The user enters: python
# #       ii. The program should print: The word python occurs 13 times
# word = input("Enter your word:")

# f = open("PythonSummary.txt", "r")
# count = 0
# masterList = [] # Take in the .split(" ") version of the list

# for x in f:
#     strList = x.split(" ")
#     masterList.extend(strList)
# f.close()

# #got through list word per word and chck for instances of python
# for x in masterList:
#     if word.upper() in x.upper():
#       count +=1

# print("The word " + word + " occurs " + str(count) + " times \n")

#4)Write a class schedule formatting program that does the following (25 points):
#   a. Parses “classesInput.txt” for the following info (on the corresponding line):
#       Line 0: Number of courses (the following data should exist for each course)
#       Line 1: Course department
#       Line 2: Course number
#       Line 3: Course name
#       Line 4: Credits
#       Line 5: Lecture days
#       Line 6: Start time of the lecture
#       Line 7: End time of the lecture
#       Line 8: Average grade (percentage) for the course
#   b. Outputs a file with the data formatted as follows:
#       COURSE 1: <Course department><Course number>:<Course name>
#       Number of Credits: <Credits>
#       Days of Lectures: <Lecture days>
#       Lecture Time: <Start time> - <End time>
#       Stat: on average, students get <average grade> in this course
#       REPEAT for each additional class, up to <Number of courses>
#   c. Example:
#       Input:
#       2
#       CSE
#       030
#       Data Structures
#       4
#       Monday, Wednesday
#       4:30pm
#       5:45pm
#       85
#       CSE
#       165
#       Introduction to Object Oriented Programming
#       4
#       Tuesday, Thursday
#       9:00am
#       10:15am
#       87

#       Output:
#       COURSE 1: CSE030: Data Structures
#       Number of Credits: 4
#       Days of Lectures: Monday, Wednesday
#       Lecture Time: 4:30pm – 5:45pm
#       Stat: on average, students get 85% in this course
#
#       COURSE 2: CSE165: Introduction to Object Oriented Programming
#       Number of Credits: 4
#       Days of Lectures: Tuesday, Thursday
#       Lecture Time: 9:00am – 10:15am
#       Stat: on average, students get 87% in this course
#   d. Note: to get full points, you must create a Python class that holds the above data and
#       has a format function that returns, or outputs the formatted text 


#define the class

# with open("classesInput.txt", "r") as file:
#     line = file.readline()
#     count = 1
#     file_contents = ""
#     while line:
#         file_contents += line
#         line = file.readline()
#         count += 1
#         print(file_contents)



#class courseInfo:#(file_input):
f = open("classesInput.txt", "r") #open(self , "r")
totalClass = f.readline().strip("\n") #Number of courses (the following data should exist for each course)

for x in range(int(totalClass)):
    #def __classBuild__(self):#define your variables
    classDept = f.readline().strip("\n")#self.f.readline().strip("\n")
    classNo = f.readline().strip("\n")#self.f.readline().strip("\n")
    className = f.readline().strip("\n")#self.f.readline().strip("\n")
    creds = f.readline().strip("\n")#self.f.readline().strip("\n")
    lectDays = f.readline().strip("\n")#self.f.readline().strip("\n")
    beginTime = f.readline().strip("\n")#self.f.readline().strip("\n")
    endTime = f.readline().strip("\n")#self.f.readline().strip("\n")
    avgGrade = f.readline().strip("\n")#self.f.readline().strip("\n")
        #__formatting__()

    #def __formatting__():#format the output
    output = "COURSE {}: {}{}: {} \nNumber of Credits: {} \nDays of Lectures: {} \nLecture Time: {} - {} \nStat: on average, students get {}% in this course \n \n" #REPEAT for each additional class, up to <Number of courses>
    print(output.format((x+1), classDept, classNo, className, creds, lectDays, beginTime, endTime, avgGrade))

    #Return a txt file
f = open("output.txt", "w")
f.write(output.format(totalClass, classDept, classNo, className, creds, lectDays, beginTime, endTime, avgGrade))
f.close()
f.close()

#Main body to call class ourse info
#file_input = "classesInput.txt"
#courseInfo(file_input)