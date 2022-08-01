fp=open('sample.txt','r')
content = fp.read()

count=1
for i in content:
    if(i=='\n'):
        count+=1

print('total lines are', count)