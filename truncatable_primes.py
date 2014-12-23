#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

from math import ceil

def p37():
    trunc_primes=0
    primes=[2,3,5,7]
    primeset=set(primes)
    current_number=11
    counter=0
    while counter < 11:
        upper_lim=int(ceil(current_number**0.5))
        add=False
        for j in primes:
            if j>upper_lim or j==primes[-1]:
                add=True
                break
            if current_number%j==0:
                break
        if add:
            add=False
            primes.append(current_number)
            primeset.add(current_number)
            left_trunc=current_number
            right_trunc=current_number/10
            power=len(str(left_trunc))-1
            while left_trunc != 0:
                if left_trunc not in primeset:
                    break
                left_trunc%=10**power
                power-=1
            while right_trunc != 0:
                if right_trunc not in primeset:
                    break
                right_trunc/=10
            if not left_trunc and not right_trunc:
                trunc_primes+=current_number
                counter+=1
        current_number+=2
    print trunc_primes
p37()
