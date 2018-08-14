#  https://www.hackerrank.com/challenges/url-hashtag-segmentation/problem
_author_ = "AJ"
file = open("words.txt", "r")
dicti = []
dicti.append(file.read().split('\n'))
newList = []
for fruit in dicti[0]:
    newList.append(fruit.lower())
dicti = tuple(newList)

def check(word):
    if(word in dicti):
        return True
    return False
    
_author_ = "AJ"
def splitter(word):
    ans = ""
    temp = []
    remtemp = [] 
    if(check(word)):
        return word
    else:
        if(len(word) != 0):
            for i in range(len(word), 0, -1):
                temp.append(word[0:i+1])
                remtemp.append(word[i+1:])
                if(check(temp[-1])):
                    break
            ans += temp[-1]
            if(remtemp[-1] != ''):
                ans = ans + ' ' + str(splitter(remtemp[-1]))

            return ans

        else:
            return ans
_author_ = "AJ"
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
_author_ = "AJ"    
