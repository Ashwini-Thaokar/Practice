import re

#extract answer section of dig command output

def printRegex():
    f= open("digout.txt", "r")
    matchObj= re.search(r"ANSWER+\s+SECTION+:\s*(.*)", f.read())
    print (matchObj.group())
    
printRegex()
