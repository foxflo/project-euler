#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

""" Again, another relatively simple dynamic programming approach. The least cost path to any point is the path
    which begins by moving right and then up/down to the target.
    
    Otherwise if we move up  or down first we could have just started from that point.

    Slight assumption: matrix in general will be square. Otherwise it's jagged and the minimal path is obvious
    if you have the path sums to the last complete column.
"""

def p82(matrix="p82.matrix"):
    matrix=open(matrix)
    matrix=[row.split(',') for row in matrix.read().split('\n')[:-1]]
    max_elem=0
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix)):
            matrix[i][j]=int(matrix[i][j])
            max_elem=max(matrix[i][j],max_elem)
    for i in xrange(1,len(matrix)):
        for j in xrange(len(matrix)):
            min_cost=max_elem*len(matrix)**2
            for k in xrange(len(matrix)):
                step=-1
                if k<j:
                    step=1
                min_cost=min(min_cost,matrix[k][i-1]+sum([matrix[l][i] for l in xrange(k,j,step)]))
            matrix[j][i]+=min_cost
    print reduce(min,[matrix[i][-1] for i in xrange(len(matrix))])
p82()
