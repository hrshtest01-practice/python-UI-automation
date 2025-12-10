"""from selenium import webdriver
strs = ["flower","flow","flight"]
a=len(strs[0])
for i in range(len(strs)):
    if len(strs[i])<len(strs[0]):
        a=i
print(a)
c=[]
b= strs[a]
count=len(b)
arr=b[0::count+1]
print(arr)
for i in range(len(strs)):
    if(arr in strs[i]):
        c.append(strs[i])
        c.append(arr)
print(c)"""



strs = ["fower","fow","folight",'foll']
a,arr=strs[0],[]
b,new=a[0],""
for i in range(1,len(a)):
    new=b+a[i]
    print(new)
    for j in strs:
        if new in j:
            arr.append(new)
        if len(arr)==len(strs):
            break
    if(len(arr)==len(strs)):
        break
    else:
        b,arr=a[i],[]
print(arr)




