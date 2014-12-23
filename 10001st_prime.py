#What is the 10 001st prime number?

def p7(n=10001):
    composite=False
    primes=[2]
    current_number=3
    while len(primes) < n:
        limit=current_number**0.5
        for i in primes:
            if i>limit:
                break
            elif current_number%i==0:
                composite=True    
                break
        if not composite:
            primes.append(current_number)
        composite=False
        current_number+=1
    print primes[-1] 
p7()
