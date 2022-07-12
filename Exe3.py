str1=input("Enter the word")
res=str1[0]
l=int(len(str1))
mi=int(l//2)
res=res+str1[mi]+str1[l-1]
print(res)