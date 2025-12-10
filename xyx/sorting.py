# find the largest one
from functools import reduce

a,x=[10,100,20,301,101],0


for i in a:
    if i>x:
        x=i
print(x)

# #    j= i+1
#     if a[i]>a[j]:
#         a[j],a[i]=a[i],a[j]
#     else:
#         a[i],a[j]=a[j],a[i]
# print(a)

b= lambda x:x%2==0
print(b(5))

z= [10,20,30,40,50,50]
c= set(map(lambda x: x*10,z))
print(c)

m= list(filter(lambda n:n%2==0,z))
print(m)

v= reduce(lambda d,f:d+f,z)
print(v)