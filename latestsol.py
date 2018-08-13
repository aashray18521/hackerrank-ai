import numpy as np

file = open("words.txt", "r")
dicti = []
dicti.append(file.read().split('\n'))
dicti = tuple(dicti[0])

def check(word):
    if(word in dicti):
        return True
    return False
    

def splitter(word):
    index = -1
    ans = ""
    temp = []
    remtemp = [] 
    if(len(word) != 0):
        for i in range(len(word), 0, -1):
            temp.append(word[0:i+1])
            index += 1
            remtemp.append(word[i+1:])
            if(check(temp[-1])):
                #print(temp[-1])
                break
        ans += temp[-1]
        if(remtemp[-1] != ''):
            #print(remtemp[-1])
            ans = ans + ' ' + str(splitter(remtemp[-1]))
        
        return ans
    
    else:
        return

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
    
    print(splitter(string))
    
