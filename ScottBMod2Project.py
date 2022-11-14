'''

  * Class: 44-141 Computer Programming I

  * Author: Brady Scott

  * Description: I will be writing a program that will calculate ppe usage. 

  * Due: Feb. 16, 11:59 P.M.

  * I pledge that I have completed the programming assignment independently.

  * I have not copied the code from a student or any source.

  * I have not given my code to any other student and will not share this code with anyone under any circumstances.

'''
#This method returns the box count for the given day.
def getboxcount(day, ppe):
    print("Please enter the number of full boxes of", end=" ")
    print(ppe, end=" ")
    print("for day", end=" ")
    print(day, end="")
    boxcount = int(input(": "))
    return boxcount

#This method returns the amount of boxes used.
def ppeusage(boxcount, totalcount):
    totalcount -= boxcount
    return totalcount

#This method returns the average amount of boxes used in a day.
def averageusage(totalppeused, totaldays):
    average = totalppeused / totaldays
    return average

#This method returns the total individual amount of ppe remaining.
def ppeleft(boxcount):
    ppeleft = boxcount * 200
    return ppeleft

#This method returns the number of days left accoding to the final box count and average used in a day.
def daysleft(boxcount, average):
    daysleft = boxcount / average
    return daysleft

#initial user instructions and input of type of ppe and the initial day which is expected to be 1.
print("This calculator returns the average number of ppe boxes used \nper day, the total number of ppe remaining, and the estimated days remaining.\nPlease start with day 1 and enter the starting quantity of boxes,\nand enter more than one day.\nCalculator assumes all ppe boxes have a ppe quantity of 200.")
ppe = input("Enter the type of PPE: ")
day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n1-mon 2-tues 3-wed 4-thurs 5-friday:\n"))
#initiallized variable
totaldays = 0
totalppeused = 0

#while loop to gather information from methods and loop through the days
while(day != 0):
    if(day == 1):
        totalcount = getboxcount(day, ppe) 
        day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n1-mon 2-tues 3-wed 4-thurs 5-friday:\n"))
    else:
        boxcount = getboxcount(day, ppe)
        totalppeused = ppeusage(boxcount, totalcount)
        day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n1-mon 2-tues 3-wed 4-thurs 5-friday:\n"))
        totaldays += 1

#Gathering information from remaining methods to be used in the output.
average = averageusage(totalppeused, totaldays)
ppeleft = ppeleft(boxcount)
daysleft = daysleft(boxcount, average)

#Output
print("average number of boxes used per day is: ", average)
print("total number of", end=" ")
print(ppe, end=" ")
print("left: ", ppeleft)
print("number of days left of", end=" ")
print(ppe, end=" ")
print(": ", int(daysleft))



    