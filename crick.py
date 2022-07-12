i=1
count=0
while i<=6:
    print("if ball then:- 101, if wide then:- 102,if no ball then: 103",i)
    code=int(input("Enter the code:- \n"))
    if code==102:
        b=int(input("how many run on wide:- "))
        run=1+b
    elif code==103:
        a=int(input("how many run on no ball:- "))
        run=1+a
    elif code==101:
        run=int(input("how many run:- "))
        i=i+1
    count=count+run
print(count)
