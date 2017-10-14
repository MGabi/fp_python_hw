import datetime as dt

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def checkLeap(year):
    return (year % 400 == 0 or year % 100 != 0) and (year % 4 == 0)


def calculateDaysFromBirthYear(y, m, d):
    if checkLeap(y):
        months[1] = 29

    days = 0
    days += months[m] - d + 1
    #print("days ", months[m], " ", days)

    for i in range(m+1, 12):
        days += months[i]
        #print("days in month ", i+1, ": ", months[i], " ", days)

    print("inBirth: ", days)
    return days


def getYearsInDays(y, cYear):
    days = 0
    for i in range(y, cYear):
        if not checkLeap(i):
            days += 365
        else:
            days += 366

    print("inYears: ", days)
    return days


def getDaysInCurrentYear(cYear, cMonth, cDay):
    days = 0
    if checkLeap(cYear):
        months[1] = 29
    else:
        months[1] = 28

    for i in range(0, cMonth-1):
        days += months[i]

    days += cDay - 1

    print("inCurrYear: ", days)
    return days


def getDaysFrom(m, d, cYear, cMonth, cDay):
    days = 0
    days += months[m] - d + 1
    if checkLeap(cYear):
        months[1] = 29
    else:
        months[1] = 28

    for i in range(m+1, cMonth-1):
        days += months[i]

    days += cDay

    return days


def calculateDays(y, m, d):
    cYear = dt.datetime.now().year
    cMonth = dt.datetime.now().month
    cDay = dt.datetime.now().day

    if m < 0 or m > 11 or d < 1 or d > 31 or y > cYear:
        return "Invalid data"

    totalDays = 0

    if y != cYear:
        totalDays = calculateDaysFromBirthYear(y, m, d)
        totalDays += getYearsInDays(y+1, cYear)
        totalDays += getDaysInCurrentYear(cYear, cMonth, cDay)
        totalDays += 1
    else:
        """totalDays += 365 - calculateDaysFromBirthYear(y, m, d)
        if checkLeap(y):
            totalDays += 1"""
        totalDays += getDaysFrom(m, d, cYear, cMonth, cDay)

    dtt = str(d) + "/" + str(m) + "/" + str(y)
    return str(totalDays) + " days have gone from " + dtt + " until today. (include current day)"


def main():
    print("Enter a date of birth to calculate the age in days: ")

    y = int(input("Year: "))
    m = int(input("Month: ")) - 1
    d = int(input("Day: "))

    print(calculateDays(y, m, d))


main()