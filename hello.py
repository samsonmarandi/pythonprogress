msg = "Hello world"
a = int(input("enter 1st number"))
b= int(input("enter 2nd number"))
c= input("enter a operator +, -, /, *")

def add(num1, num2):
    return num1+num2


def subtract(num1, num2):
    return num1-num2


def div(num1, num2):
    return num1/num2


def mult(num1, num2):
    return num1*num2


if(c=="+"):
    result = add(a,b)
    print("sum is ",result)

elif(c=="-"):
    result = subtract(a,b)
    print("subraction is ", result)

elif(c=="/"):
    result= div(a,b)
    print("division is ",result)

elif(c=="*"):
    result= mult(a,b)
    print("multiplication is ", result )

else:
    print("wrong operator")
