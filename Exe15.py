def count(list1,num):
    count=0
    for i in list1:
        if i==num:
            count=count+1
    return count
Z=count([1,2,1,1],1)
print(Z)
