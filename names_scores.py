#What is the total of all the name scores in the file?

""" Thankfully, python has a built in alphabetical sorter for lists :)
"""

def p22(names="p22.names"):
    nameFile=open(names)
    names=nameFile.read()[1:-1].split('","') # we slice [1:-1] for easy splitting 
    nameFile.close()
    names.sort()
    total_score=0
    for i in xrange(len(names)):
        name_score=0
        for character in names[i]:
            name_score+=ord(character)
        name_score-=len(names[i])*64
        name_score*=(i+1)
        total_score+=name_score
    print total_score
p22()
