#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#Ugh.

#1 January 1901 was a Tuesday (day 2)

from collections import defaultdict

def p19():
    special_sundays=0
    x=defaultdict(lambda:31)
    x[3],x[5],x[8],x[10]=30,30,30,30
    month,day,day_of_week,year=0,0,1,1901
    while year < 2001:
        if year%4==0 and (year%100!=0 or year%400==0):
            x[1]=29
        else:
            x[1]=28
        while month < 12:
            while day < x[month]:
                if day==0 and day_of_week==6:
                    special_sundays+=1
                day += 1
                day_of_week=(day_of_week+1)%7
            month+=1
            day=0
        year+=1
        month=0
    print special_sundays
p19()
