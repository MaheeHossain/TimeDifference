# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Gets the two times and gets the difference

#25/04/1924 19:18:42.024
#14/05/2005 20:15:23.425

#import printTimes
from timeFunctions.timeConstants import STRING_SPLITTERS
import timeFunctions.timeConstants as timeConstants
from timeFunctions.printTimes import printBothTimeArrays

def differenceInTimes(times): 
    # Break the times into arrays with helper function splitDate
    # Day/Month/Year Hours:Minutes:Seconds.Microseconds
    timeA = splitDate(times[0])
    timeB = splitDate(times[1])
    printBothTimeArrays(timeA, timeB)
    return 0

def splitDate(time):
    for splitter in timeConstants.STRING_SPLITTERS:
        time = time.replace(splitter, " ")
    return time.split(' ')[timeConstants.DAY:timeConstants.MICROSECOND+1]