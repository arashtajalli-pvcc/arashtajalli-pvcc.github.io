# Name: Arash_Tajalli
# Program Purpose: Extract data from the date & time
# The three lines below help to find the string positions
# 00000000001111111111222222
# 01234567890123456789012345
# 2023-11-08 19:51:43.993231

import datetime

def main():
    today = str(datetime.datetime.now())

    year = today[0:4]
    month = today[5:7]
    day = today[8:10]
    day_time = today[0:16]

    print("Full date/time: "+ today)
    print("\tYear:         " + year)
    print("\tDay:          " + day)
    print("\tDay & Time:   " + day_time)

    cal_months = ["January", "February", "March", "April", "May","June","July","August","September","October","November","December"]
    monthname = cal_months[int(month)-1]
    ## Test for sequence continuity in calmonths
    ##calmonnum=0
    ##while calmonnum!=12:
        ##print(cal_months[calmonnum])
        ##calmonnum +=1
    print("\t" + monthname + " " + day + ", " + year)
    exit()

main()