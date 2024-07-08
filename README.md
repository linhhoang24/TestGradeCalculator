# TEST GRADE CALCULATOR

## Introduction
This program is used to to calculate the test scores (multiple choice test) based on students' answers and to perform the results analysis. The expected outcomes of the program should be:
* A report summarizes the key information of the data including overview of the data and statisical analysis of the test results.
* An additional report contains further details for invalid data.
* A generated text file to store the test result of every student.

## How to use
### Prepare the data files
Valid data file should:
* Contain student ID and answers only
* Have each line containing information of a single student and using the comma (",") as the separator

### Run the program
**Step 1:** Open the programm with python runner application\
**Step 2:** When you see the command `Enter a class file to grade (i.e. class1 for class1.txt):`, please enter the file name\
**Step 3:** Let the program run and return the report to you.The generated file of students' test results are stored in the same folder as your orginal data files.

## Futher notes
* The program file (python file) should be saved in the same folder as all the data files
* The program is written for a test of 25 multiple choices questions. Therefore, it is essential to adjust the code if the test length changes.
* The default student ID is of the format **N########** - an **N** followed by 8 numbers. Therefore, it is essesntial to adjust the code if the student ID's format changes.

