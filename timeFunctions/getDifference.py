# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Gets the two times and gets the difference

from timeFunctions.timeConstants import STRING_SPLITTERS
import timeFunctions.timeConstants as timeConstants
from timeFunctions.printTimes import printBothTimeArrays
import datetime

def differenceInTimes(times): 
    # Break the times into arrays with helper function splitDate
    # Day/Month/Year Hours:Minutes:Seconds.Microseconds
    timeA = turnArrayIntoDatetime(splitDate(times[0]))
    timeB = turnArrayIntoDatetime(splitDate(times[1]))
    #printBothTimeArrays(timeA, timeB)
    print(timeA)
    return orderThenDifferntiateTimes(timeA, timeB)

def orderThenDifferntiateTimes(timeA, timeB):
    # First order the times, then differentiate them
    # Year
    
    return 0

def splitDate(time):
    for splitter in timeConstants.STRING_SPLITTERS:
        time = time.replace(splitter, " ")
    return time.split(' ')[timeConstants.DAY:timeConstants.MICROSECOND+1]

def turnArrayIntoDatetime(time):
    # Take the time array and turn it into a datetime
    date = datetime.datetime(
        int(time[timeConstants.YEAR]),
        int(time[timeConstants.MONTH]),
        int(time[timeConstants.DAY]),
        int(time[timeConstants.HOUR]),
        int(time[timeConstants.MINUTE]),
        int(time[timeConstants.SECOND]),
        microsecondMultiplier(time[timeConstants.MICROSECOND])
    )
    return date

def microsecondMultiplier(microseconds):
    # Depending on how many digits the decimal point is, 
    # fit it to the datetime format
    digits = len(microseconds)
    multiplier = timeConstants.MICROSECOND_MULTIPLIER / (10 ** digits)
    return int(int(microseconds) * multiplier)