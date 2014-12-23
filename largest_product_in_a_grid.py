#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?


""" If the matrix were larger (as in computationally expensive), one could speed up computations by:
    finding all zeroes in matrix, mark all numbers vertically, horizontally, and left diagonally that are n or fewer
    spaces away. Then in computation just ignore marked positions
    
    Alternatively, perform each type of computation individually (that is, do all horizontal, all vertical, etc.)
    Then in each we can reuse the algorithm from problem 8.
"""

def p11(n=4):
    grid=open("p11.grid")
    matrix=grid.read().split('\n')
    grid.close()
    if len(matrix[-1])==0:   
        matrix=matrix[:-1]
    new_matrix=[]
    for row in matrix:
        new_matrix.append(row.split())
    for i in xrange(len(new_matrix)):
        for j in xrange(len(new_matrix[i])):
            new_matrix[i][j]=int(new_matrix[i][j])
    max_product=0
    for i in xrange(len(new_matrix)):
        for j in xrange(len(new_matrix[i])):
            if j <= len(new_matrix[i])-n:
                temp_product=1
                for k in xrange(n):
                    temp_product*= new_matrix[i][j+k]
                max_product=max(max_product,temp_product)
            if i <= len(new_matrix)-n:
                temp_product=1
                for k in xrange(n):
                    temp_product*=new_matrix[i+k][j]
                max_product=max(max_product, temp_product)
                if j <= len(new_matrix[i])-n:
                    temp_product=1
                    for k in xrange(n):
                        temp_product*=new_matrix[i+k][j+k]
                    max_product=max(max_product, temp_product)
                if j >= n:
                    temp_product=1
                    for k in xrange(n):
                        temp_product*=new_matrix[i+k][j-k]
                    max_product=max(max_product,temp_product)
    print max_product
p11()
