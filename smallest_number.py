from cgitb import small


num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))
# 15,10,5

list = [num1,num2,num3]
def findSmallestNum():
    for i in range(0,len(list)-1):
         for j in range(0, len(list)-1):
                if list[j]>list[j+1] :                    
                    temp=list[j]
                    list[j]=list[j+1] 
                    list[j+1]=temp
                    print('one')
              

findSmallestNum()
print("smallest number is",list[0])

