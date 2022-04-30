def courseAnalyse(courses):
    sum = 0
    failcount = 0
    for i in range(len(courses)):
        sum = sum + courses[i][1]
        if courses[i][1] >= 90:
            print("\nExcellent Job! You got A in " + courses[i][0] + "!")
        elif courses[i][1] >= 60:
            print("\nGood job! You passed the exam in " + courses[i][0] + "!")
        else:
            failcount = failcount +1
            print("\nSorry! You failed in " + courses[i][0] + "! You need to retake it.")
            
    average = sum/len(courses)
    
    if failcount > 0:
        print("\nYou have " + str(failcount) + " course(s) failed! Please work harder!")
    else:
        print("\nCongratulations! You passed all exams!")
    
    return average


# myCourses is a two dimentional list, thich stores the subjects and scores the student took

choice = str(input("\nDo you want to input your courses scores? (Y/N) ")).upper()
while choice == 'Y':
    
    myCourses = []
    numCourses = int(input("How many courses did you take? "))

    for i in range(numCourses):
        coursename = str(input("\nPlease input the name of your course "+ str(i+1)+": "))
        coursescore = int(input("\nPlease input the score of "+ coursename + ": "))
        myCourses.append([coursename,coursescore])
    
    print("\nThe courses you took:\n")
    print(myCourses)
    
    averageScore = courseAnalyse(myCourses)
    print("\nYour average score is "+ str(averageScore))
    choice = str(input("\nDo you want to input more courses scores? (Y/N) ")).upper()
