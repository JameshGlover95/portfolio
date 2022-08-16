import re
import string
words = [] #initiate a list for the list of words in the file
norepwords = {}
def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

def printItems():
    file = open('input.txt')
    for i in file: #loops though the values in the file
        words.append(i.rstrip('\n'))    #adds the values to a list
    
    for i in words: # loops though the list of all words
        if i in norepwords: #allows the loop to skip repeated words 
            continue 
        else: # adds a word to the list of words skipping repeated words
            norepwords[i] = words.count(i)

    for k,v in norepwords.items(): # loop to print the words in the list of nonrepeated words and numer of occuances in the file
                print(k,v)
    file.close()

def findItem(v):
    num = 0
    file = open('input.txt')

    for l in file: #loops though the values in the file
        words.append(l.rstrip('\n'))    #adds the values to a list
    
    for w in words: # loops though the list of all words
        if w in norepwords: #allows the loop to skip repeated words 
            continue 
        else: # adds a word to the list of words skipping repeated words
            norepwords[w] = words.count(w)
        for k in norepwords.keys(): #loops thgough the dict keys and chaecks the input in all lower case to the input isnt case sensitive
            if k.lower() == v.lower(): 
                 num = norepwords.get(k) 
    return num #returns the count to c++
        
    file.close()

            
def frequency():
    outfile = open("frequency.dat", "w")
    file = open('input.txt')
    for i in file: #loops though the values in the file
        words.append(i.rstrip('\n'))    #adds the values to a list
    
    for i in words: # loops though the list of all words
        if i in norepwords: #allows the loop to skip repeated words 
            continue 
        else: # adds a word to the list of words skipping repeated words
            norepwords[i] = words.count(i)

    for k,v in norepwords.items(): # loop to print the words in the list of nonrepeated words and nubmer of occuances in the file
        temp = k + " " + str(v) + "\n"
        outfile.write(temp)

    file.close()
    outfile.close()
        
        

   