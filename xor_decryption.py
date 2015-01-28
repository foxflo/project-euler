#decrypt the message and find the sum of the ASCII values in the original text

def p59(cipher="p59.cipher"):
    cipher=open(cipher)
    cipher=[int(i) for i in cipher.read().split('\n')[0].split(',')]
    cipher1=[cipher[i] for i in xrange(0,len(cipher),3)]
    cipher2=[cipher[i] for i in xrange(1,len(cipher),3)]
    cipher3=[cipher[i] for i in xrange(2,len(cipher),3)]
    
p59()
