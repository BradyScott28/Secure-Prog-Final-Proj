'''

  * Class: 44-141 Computer Programming I

  * Author: Brady Scott

  * Description: I will be writing a program that will calculate ppe usage. 

  * Due: Feb. 16, 11:59 P.M.

  * I pledge that I have completed the programming assignment independently.

  * I have not copied the code from a student or any source.

  * I have not given my code to any other student and will not share this code with anyone under any circumstances.

'''
#This part records the type of PPE you are using and sets base variables
ppe = input("Enter the type of PPE: ")
day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n1-mon 2-tues 3-wed 4-thurs 5-friday:\n"))
totaldays = 0
ppeused = 0
totalppeused = 0

#This is my while looop to gather information for eact day of the week
while(day != 0):
    if(day == 1):#This part gets the initial amount of of ppe(totalnum)
        print("Please enter the number of full boxes of", end=" ")
        print(ppe, end=" ")
        print("for day", end=" ")
        print(day, end="")
        totalnum = int(input(": "))
        day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n1-mon 2-tues 3-wed 4-thurs 5-friday:\n"))
    else:#This part continues with the loop for the remainig days
        print("Please enter the number of full boxes of", end=" ")
        print(ppe, end=" ")
        print("for day", end=" ")
        print(day, end="")
        num = int(input(": ")) 
        ppeused = totalnum - num #calculates amount of ppe used to calculate the total ppeused
        totalppeused +=ppeused #calculates totalppeused to be used to find the average ppe used
        totalnum -= ppeused #calulates the amount of ppe remaining after that day
        day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n1-mon 2-tues 3-wed 4-thurs 5-friday:\n"))
        totaldays += 1 #records total number of days entered

#This is final part of the code that calculates the averages, ppe left, and the days left of the PPE0
average = totalppeused / totaldays
print("average number of boxes used per day is: ", average)
print("total number of", end=" ")
print(ppe, end=" ")
print("left: ", totalnum * 200)
print("number of days left of", end=" ")
print(ppe, end=" ")
print(": ", int(totalnum/average))
      



    