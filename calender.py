# function to get the number of days in a month
# function to print the month
# function to print the whole calender of the year
def printMonth(monthNumber):
    print("SUN\tMON\tTUE\tWED\tTHU\tFRI\tSAT\n")
    print("----------------------------------------------------------------")
    days = 31
    startingDay = 1
    dayCounter = 1

    while(dayCounter <= days):
        if(dayCounter % 7 == 0):
            print(str(dayCounter) + "\t",end='')
            print("\n")
        else:
            print(str(dayCounter) + "\t",end='')
        dayCounter+=1


def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def numberOfDayInAMonth(month,year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or  month == 12:
       return 31
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
       return 30
    else:
        # invalid month
        return -1
    
def findTheFirstDayOfTheMonth(day,month,year):
    # Zeller’s Congruence Formula:
    
    # q - day of the month
    # m - month number 3 = march, 4 = april, ... 12 = dec, 13 = january of the previous year, 14 = febrary of the previous year
    # K - year of the century (year % 100)
    # J - zero based century (year/100)

    q = -1
    m = -1
    K = -1
    J = -1

    q = day 

    if month == 1:
       year -= 1
       m = 13
    elif month == 2:
        year -= 1
        m = 14
    else:
        m = month
    
    K = year % 100
    J = year // 100

    h = (q + (13*(m+1)//5) + K + (K//4) + (J//4) - 2*J) % 7
    return ((h - 1) + 7) % 7
    # return h

# days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']

# for year in range(2000,2025):
#     h = findTheFirstDayOfTheMonth(1,1,year)
#     print(year,' - ' , h, days[h])
def printEmptySpace(gaps):
    if gaps > 0:
       for i in range(gaps):
           print("  " + "\t",end='')

def printMonthName(month):
    names = ['January','February','March','April','May','June','July','August','September','October','November','December']
    print("\t\t      " + names[month-1])
    print()

def printMonth(month,year):
    printMonthName(month)
    print("SUN\tMON\tTUE\tWED\tTHU\tFRI\tSAT")
    print("---------------------------------------------------")
    days = numberOfDayInAMonth(month,year)
    startingDay = findTheFirstDayOfTheMonth(1,month,year)
    dayCounter = 1

    printEmptySpace(startingDay)

    while(dayCounter <= days):
        print(str(dayCounter) + "\t", end='')
        if (startingDay + dayCounter) % 7 == 0:
            print("")
        dayCounter += 1
    
    print("\n")
    
def printYear(year):
    print("\t\t\t" + str(year))
    print()
    for i in range(1,13):
        printMonth(i,year)
    
print("Choose one of the options: ")
print("1. Year")
print("2. Month")
choice = input("\nEnter your choice 1 or 2:")

if int(choice) == 1:
   year = int(input("Enter the year: "))
   printYear(year)
else:
   year = int(input("Enter the year: "))
   month = int(input("Enter month number: "))
   printMonth(month,year)


