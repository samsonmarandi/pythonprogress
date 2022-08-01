str= input("enter a string")
str2= input("enter a character")

def remchar(char, str):
    temps=""
    for i in str:
        if(i!=char):
            temps+=i
        
    
    return temps
        


print(remchar(str2, str))