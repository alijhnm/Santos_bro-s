from random import *
a=randrange(1,1001)
c=1
while True :
    b=int(input('  ? : '))
    if a<b :
        print ('boro paien')
        c=c+1
    if a>b :
        print('boro bala')
        c=c+1
    if a==b :
        print('A Mashala')
        print(c,'ta hads tool keshid ta be javab beresi')
        break

        
