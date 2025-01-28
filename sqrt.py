year = int(input("year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"the {year} is leap year ")
else:
    print(f"the {year} is not leap year ")