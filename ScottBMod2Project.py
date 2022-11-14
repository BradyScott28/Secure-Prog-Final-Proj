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

#Since the variable ppe is just used as a reference name, no user input is needed
#Therefor the first user input would be for the day which must be 1.
def userInput1(day):    
    while True:
        try:
            day = int(day)
        except:
            print("Please enter the integer '1' for the first day entry")
            day = int(input("Enter the number 1 for the first monday, the first day of the entry, or 0 to quit\n"))
            userInput1(day)
        if(day == 0):
            print("You have chosen to quit the program. Thank you.")
            quit()
        if(day != 1):
            print("Please enter day '1' first")
            day = int(input("Enter the number 1 for the first monday, the first day of the entry, or 0 to quit\n"))
            userInput1(day)
        break
#second user input to verify proper day is used for remaining days
def userInput2(day):   
    while True:
        try:
            day = int(day)
        except:
            print("Please enter a integer for the day entry between 2-5")
            day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n2-tues 3-wed 4-thurs 5-friday:\n"))
            userInput2(day)
        if(day == 1):
            print("You have already inputted for day 1")
            day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n2-tues 3-wed 4-thurs 5-friday:\n"))
            userInput2(day)
        if(day < 0):
            print("Enter a number within the range")
            day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n2-tues 3-wed 4-thurs 5-friday:\n"))
            userInput2(day)
        if(day > 5):
            print("Enter a number within the range")
            day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n2-tues 3-wed 4-thurs 5-friday:\n"))
            userInput2(day)
        break

#initial user instructions and input of type of ppe and the initial day which is expected to be 1.
print("This calculator returns the average number of ppe boxes used \nper day, the total number of ppe remaining, and the estimated days remaining.\nPlease start with day 1 and enter the starting quantity of boxes,\nand enter more than one day.\nCalculator assumes all ppe boxes have a ppe quantity of 200.")
ppe = input("Enter the type of PPE: ")
day = int(input("Enter the number 1 for the first monday, the first day of the entry, or 0 to quit\n"))
userInput1(day)
#Since the variable ppe is just used as a reference name, no user input is needed
#Therefor the first user input would be for the day which must be 1.

        
#initiallized variable
totaldays = 0
totalppeused = 0

#while loop to gather information from methods and loop through the days
while(day != 0):
    if(day == 1):
        totalcount = getboxcount(day, ppe) 
        day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n2-tues 3-wed 4-thurs 5-friday:\n"))
    else:
        boxcount = getboxcount(day, ppe)
        totalppeused = ppeusage(boxcount, totalcount)
        day = int(input("Enter the number that corresponds to the day of the week you would like to\nenter for or 0 to quit\n2-tues 3-wed 4-thurs 5-friday:\n"))
        totaldays += 1
    userInput2(day)
        

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


