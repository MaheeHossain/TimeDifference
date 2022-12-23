import timeFunctions.timeConstants as arrayPosition

def printBothTimeArrays(timeA, timeB):
    print("FIRST TIME")
    printTimeArray(timeA)
    print("\nSECOND TIME")
    printTimeArray(timeB)

def printTimeArray(time):
    print("Day: {}".format(time[arrayPosition.DAY]))
    print("Month: {}".format(time[arrayPosition.MONTH]))
    print("Year: {}".format(time[arrayPosition.YEAR]))
    print("Hour: {}".format(time[arrayPosition.HOUR]))
    print("Minutes: {}".format(time[arrayPosition.MINUTE]))
    print("Seconds: {}".format(time[arrayPosition.SECOND]))
    print("Microseconds: {}".format(time[arrayPosition.MICROSECOND]))