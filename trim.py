sentence=input("enter a string")


def removeLeftSpace(s):
    
    while s[0]==" ":
        temps=""
        for i in range(1, len(s)):
            temps+=s[i]
        s=temps

    return s

def removeRightSpace(s):

    while s[(len(s)-1)]==" ":
        temps=""
        for i in range(0, len(s)-1):
            temps+=s[i]
        s=temps

    return s

def trim(s):
    str=s

    str=removeLeftSpace(str)
    str=removeRightSpace(str)

    return str



print(trim(sentence))