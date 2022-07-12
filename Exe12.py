def addition(num):
    if(num==1):
        return 1
    else:
        return num*addition(num-1)
x=int(input("Enter the number"))
z=addition(x)
print(z)