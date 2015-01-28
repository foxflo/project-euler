#Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

from math import ceil, sqrt

def p47(n=4):
    primes=[2,3,5,7]
    curr_num=10
    consecutive=0
    while True:
        num_divisors=0
        temp=curr_num
        for i in primes:
            if temp==1:
                break
            if not temp%i:
                num_divisors+=1
            while not temp%i:
                temp/=i
        if num_divisors==n:
            consecutive+=1
        else:
            consecutive=0
        if temp==curr_num:
            primes.append(curr_num)
            curr_num+=1
            continue
        if consecutive==n:
            print curr_num-n+1
            return
        curr_num+=1
p47()
