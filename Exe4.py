str1=input("Enter the word:-  \n")
l=int(len(str1))
mi=int(l//2)
first=int(mi-1)
#print(str1[mi])
end=int(mi+1)
print(str1[end])
res=str1[first]+str1[mi]+str1[end]
print(res)