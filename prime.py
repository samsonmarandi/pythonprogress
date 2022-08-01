num = int(input("enter a number"))

def checkPrime(a): 
            isP = True
            for i in range(2,a):
                if(int(num%i) == 0):
                    isP=False
            return isP
                

result = checkPrime(int(num/2+1))

if(result == True):
    print(num, "is a prime number")
else :
    print(num, "is not prime number")
