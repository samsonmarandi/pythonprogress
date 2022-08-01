import time

def min(m):
    if(m<10):
        return f"0{m}"
    elif (m>=10):
        return m

def sec(s):
    if(s<10):
        return f"0{s}"
    elif(s>=10):
        return s

def convert(t):
    m=int(t/60)
    s=t%60
    return f"{min(m)}:{sec(s)}"

def countDown(t):
    while t>=0:
        print(convert(t))
        time.sleep(1)
        t-=1


t = int(input("enter countdown time in seconds "))
countDown(t)

