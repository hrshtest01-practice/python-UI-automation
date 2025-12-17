a=[1,2,3,87,55,4,3,3,2,3,5,6]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)