import numpy as np
import pandas as pd

#TASK1: Open and read file txt using try/except
filename = input("Enter a class file to grade (i.e. class1 for class1.txt):")
fileFullName = filename +'.txt'
try:
    file = open(fileFullName,"r")
    print("Successfully opened", fileFullName)
except:
    print("File cannot be found.")


#TASK2: Analyzing the file and make report
# Each line contains information of a student, then transform each line into a list
fileContent = file.readlines()
fileContent = [line.rstrip() for line in fileContent] # truncate the newline \n at the end of each line

# ANALYZING
print('**** ANALYZING ****')
validLines = 0
invalidLines = 0
validTest = [] # list of student's tests that are valid
for line in fileContent:
    newline = line.split(',') # Each line then transformed into a sublist.
    condition1 = "False"
    condition2 = "False"
    if len(newline) == 26: # Set condition for valid list length of 26 members
        condition1 = "True"
    if len(newline[0]) == 9 and newline[0][0] == "N" and newline[0][1:].isnumeric(): # Set condition for valid studentID
        condition2 = "True"

    # check every line
    if condition1 == "True" and condition2 == "True":
        validLines += 1
        validTest.append(line)
    elif condition1 != "True" and condition2 == "True":
        invalidLines += 1
        print('Invalid line of data: does not contain exactly 26 values')
        print(line)
    elif condition1 == "True" and condition2 != "True":
        invalidLines += 1
        print('Invalid line of data: N# is invalid')
        print(line)
    else:
        invalidLines += 1
        print('Invalid line of data: N# is invalid and line does not contain exactly 26 values')
        print(line)

if validLines == len(fileContent): # Check if all lines are valid
    print('No errors found!')

# REPORT
print('**** REPORT ****')
print('Total valid lines of data:', validLines)
print('Total invalid lines of data', invalidLines)


# TASK3: Grading
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.split(',')

gradeList = {} # a dictionary to save all the studentID (key) together with his/her final grade (value)
skipList = [] # a list contains skipped questions
incorrectList = [] # a list contains questions that are answered incorrectly

# Calculate the grade
for line in validTest:
    newline = line.split(',') # Each line then transformed into a sublist.
    grade = 0
    start = 1
    # print(newline)
    while start <=25:
        if newline[start] == answer_key[start-1]:
            grade += 4
        elif newline[start] == '':
            grade += 0
            skipList.append(start)
        else:
            grade -= 1
            incorrectList.append(start)
        start += 1
    gradeList[newline[0]] = grade
# print(gradeList)


grades = list(gradeList.values())
# Total student of high scores
totalHighScore = 0
for i in range(len(grades)):
    if grades[i] > 80:
        totalHighScore += 1
print('Total students with high scores:', totalHighScore)

# Mean (average) score
totalGrade = 0
for i in range(len(grades)):
    totalGrade += grades[i]
meanScore = totalGrade/len(grades)
print('Mean (average) score:', meanScore)

# Highest score
print('Highest score:', max(grades))

# Lowest score
print('Lowest score:', min(grades))

# Range of scores
print('Range of scores:', max(grades) - min(grades))

# Median score
grades = sorted(grades)
if len(grades)%2 == 1:
    idx_median = int((len(grades) - 1)/2)
    medianScore = grades[idx_median]
else:
    idx_median1 = int(len(grades)/2)
    idx_median2 = int(len(grades)/2 - 1)
    medianScore = (grades[idx_median1] + grades[idx_median2])/2
print('Median score:', medianScore)

# Question that most people skip
# Count the skipped times for each question
skipCount = {}
for question in skipList:
    if question in skipCount:
        skipCount[question] += 1
    else:
        skipCount[question] = 1

# Find the questions with the highest skipped times
maxSkipCount = max(skipCount.values())
maxSkippedQuestions = []
for question, count in skipCount.items():
    if count == maxSkipCount:
        maxSkippedQuestions.append(question)
maxSkippedQuestions.sort()

print('Question that most people skip: ', end="")
print(', '.join(f"{question} - {maxSkipCount} - {round(maxSkipCount/validLines, 3)}" for question in maxSkippedQuestions))

# Question that most people answer incorrectly
incorrectCount = {}
for question in incorrectList:
    if question in incorrectCount:
        incorrectCount[question] += 1
    else:
        incorrectCount[question] = 1
        
# Find the questions with the highest incorrect answers
maxIncorrectCount = max(incorrectCount.values())
maxIncorrectAnsweredQuestions = []
for question, count in incorrectCount.items():
    if count == maxIncorrectCount:
        maxIncorrectAnsweredQuestions.append(question)
maxIncorrectAnsweredQuestions.sort()

print('Question that most people answer incorrectly: ', end="")
print(', '.join(f"{question} - {maxIncorrectCount} - {round(maxIncorrectCount/validLines, 3)}" for question in maxIncorrectAnsweredQuestions))


# TASK4: Create result file
resultfile = filename + "_grade.txt"
with open(resultfile, 'w') as writefile:
    for student, grade in gradeList.items():
        writefile.write(f"{student}, {grade} \n")