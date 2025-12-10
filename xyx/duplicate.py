numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
a={}
for i in numbers:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
z=[]
for k,l in a.items():
    if l>1:
        z.append(k)
print(z)