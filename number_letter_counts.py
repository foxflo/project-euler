#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

letters={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}

""" This one is not done in general, but could easily be generalized by including more checks about the input
    Since it's quite repetitive after you've done the first "set" of numbers
"""

def p17(n=1000):
    count=0
    for i in xrange(100):
        if i < 21:
            count += letters[i]
        else:
            count += letters[i/10*10]+letters[i%10]
    count*=10
    temp=0
    for i in xrange(10):
        temp+=letters[i]
    count+=100*temp
    count+=99*3*9  #ands
    count+=100*7*9 #hundreds
    count+=3+8     #one thousand
    print count
p17()
