#What is the first term in the Fibonacci sequence to contain 1000 digits?

""" Again, thank guido for python's implicit arbitrary precision integers (a common theme, eh)

    To be more clever, we could try to exploit the golden ratio to calculate the appropriate term
    but this is mostly equivalent to the current situation since we need a lot of precision for that as well
    (to calculate using real numbers, we technically need  infinite precision).
"""

def p2(n=1000):
    a,b=1,1
    term_num=2
    while True:
        a+=b
        if len(str(a)) > 999:
            print term_num+1
            return
        b+=a
        if len(str(b)) > 999:
            print term_num+2
            return
        term_num+=2
p2()
