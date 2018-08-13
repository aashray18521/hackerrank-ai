import numpy as np

file = open("words.txt", "r")
dicti = []
dicti.append(file.read().split('\n'))
dicti = tuple(dicti[0])

def check(word):
    if(word in dicti):
        print("True"+" "+word)
    return
    
temp = []
remtemp = [] 
def splitter(word):
    for i in range(len(word)):
        global temp.append(word[0:i+1])
        global remtemp.append(word[i+1:])
    global temp = global temp[::-1]
    

t = int(input())
while(t):
    t -= 1
    string = input()
    if(string.find('.')):
        string = string.split('.')
        if(('www') in string):
           string.drop('www')
        string = string[0]
    else:
        string = string.split('#')
        string = string[1]
        
    #for i in range(0, len(string)):
    #    print(string[0:i+1])
    
    splitter(string)
    
    
    #print(temp)
    #print(remtemp)
    for i in range(len(global temp)):
        check(global temp[i])
    
    #print(dicti)
    del temp[:]
    del remtemp[:]
    
    
    #print(string)
