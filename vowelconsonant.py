from asyncio import constants


str = input("enter a sentence")

vowel=0
consonant=0
for i in range(0, len(str)):
    if(str[i]=='a' or str[i]== 'A' or str[i]=='e' or str[i]== 'E' or str[i]=='i' or str[i]== 'I' or str[i]=='o' or str[i]== 'O' or str[i]=='u' or str[i]== 'U'):
        vowel+=1
    elif((int(ord(str[i]))>=65 and int(ord(str[i]))<=90) or int(ord(str[i])>=97 and int(ord(str[i]))<=122)):
        consonant+=1


print("vowel ", vowel)
print("consonant ", consonant)

