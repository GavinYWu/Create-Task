# "courses" is the local variable of "myCourses"
def courseAnalyse(courses):
    sum = 0
    passcount = 0
    failcount = 0
    for i in range(len(courses)):
        sum = sum + courses[i][1]
        if courses[i][1] >= 90:
            print("\nExcellent Job! You got A in " + courses[i][0] + "!")
            passcount = passcount + 1
        elif courses[i][1] >= 60:
            print("\nGood job! You passed the exam in " + courses[i][0] + "!")
            passcount = passcount + 1
        else:
            failcount = failcount + 1
            print("\nSorry! You failed in " + courses[i][0] + "! You need to retake it.")
                
    if failcount > 0:
        print("\nYou passed " + str(passcount) + " course(s) and failed "+ str(failcount) + " course(s)! Go study harder!")
    else:
        print("\nCongratulations! You passed all exams!")
    
    return sum/len(courses)


# myCourses is a two dimensional list, which stores the subjects and the corresponding scores the student takes

choice = str(input("\nDo you want to input your courses scores? (Y/N) ")).upper()
while choice == 'Y':
    
    myCourses = []
    try:
      numCourses = int(input("How many courses did you take? "))
    except ValueError:
      print("That was not a valid number, please try again.")
      continue

# the user input the name and grade of each course, then add it to the 2-D list "myCourses"
    for i in range(numCourses):
        coursename = str(input("\nPlease input the name of your course "+ str(i+1)+": "))

        while True:
            try:
                coursescore = float(input("\nPlease input the score of "+ coursename + ": "))
                break
            except ValueError:
                print("That was not a valid number, please try again.")
            
        myCourses.append([coursename,coursescore])
    
    
    print("\nYour average score is "+ str(courseAnalyse(myCourses)))
  
    choice = str(input("\nDo you want to input more courses scores? (Y/N) ")).upper()
