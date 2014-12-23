#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

def p8(n=13):
    number=open("p8.number")
    x="".join(number.read().split()   )
    number.close()
    product=0
    counter,index=0,0
    current_product=1
    while index <= len(x)-n:
        while counter < n:
            if x[counter+index]!='0':
                current_product*=int(x[index+counter])
                counter+=1
            else:
                index=index+counter+1
                if index > len(x)-n:
                    current_product=0
                    counter=n
                else:
                    current_product=1
                    counter=0
        product=max(product, current_product)
        index=index+counter
        counter=0
        while index < len(x) and x[index]!='0':
            current_product*=int(x[index])
            current_product/=int(x[index-n])
            product=max(product, current_product)
            index+=1
        current_product=1
    print product
p8(13)
