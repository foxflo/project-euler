#How many words in p42.words are triangle words?

from collections import defaultdict

def p42(words="p42.words"):
    words=open(words)
    all_words=words.read().strip()
    words.close()
    words= all_words[1:-1].split('","')
    
    max_len=0
    for word in words:
        max_len=max(max_len,len(word))
    max_value=max_len*26
    
    letter_indices={}
    for i in xrange(65,91):
        letter_indices[chr(i)]=i-64
    
    triangulars=defaultdict(lambda:0)
    counter=2
    curr_triang=1
    while curr_triang < max_value:
        triangulars[curr_triang]=1
        curr_triang=counter*(counter+1)/2
        counter+=1
    
    print sum([triangulars[sum([letter_indices[i] for i in word])] for word in words])
p42()
