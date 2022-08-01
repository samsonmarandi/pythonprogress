import random
import time
passwordLength = int(input('enter length of your password'))



def generatePassword(passwordLength) :
    password = ''
    for i in range(0, passwordLength):
        randomNum = random.randint(33, 122)
        password=password+str(chr(randomNum))
    return password

start=(time.time_ns())
password = generatePassword(passwordLength)
print("your password is", password)
end=time.time_ns()-start
print(end)