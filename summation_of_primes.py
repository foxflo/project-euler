#Find the sum of all the primes below two million.

def p10(n=2000000): 
    composite=False
    primes=[2]
    prime_sum=2
    current_number=3
    while current_number < n:
        limit = current_number**0.5
        for i in primes:
            if i > limit:
                break
            if current_number%i==0:
                composite=True    
                break
        if not composite:
            primes.append(current_number)
            prime_sum+=current_number
        composite=False
        current_number+=1
    print prime_sum
p10()
