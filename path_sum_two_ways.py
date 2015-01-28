#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

""" simple dynamic programming approach
"""

def p81(matrix="p81.matrix"):
    matrix=open(matrix)
    matrix=[row.split(',') for row in matrix.read().split('\n')[:-1]]
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            matrix[i][j]=int(matrix[i][j])
    for i in xrange(1,2*len(matrix)-1):
        for j in xrange(i+1):
            if j >= len(matrix):
                break
            if i-j >= len(matrix[j]):
                continue
            if j-1<0:
                matrix[j][i-j]+=matrix[j][i-j-1]
            elif i-j-1<0:
                matrix[j][i-j]+=matrix[j-1][i-j]
            else:
                matrix[j][i-j]+=min(matrix[j-1][i-j],matrix[j][i-j-1])
    print matrix[-1][-1]
p81()
