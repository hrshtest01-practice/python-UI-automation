"""b=[5,5,3,2,1,6]
count=len(b)

for i in range(count):
    for j in range(count-1):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
print(b)"""
"""
l = [item + 1 for item in range(10)]
for item in l:
   # print(item)
   pass
g = (item + 1 for item in range(10))
for item in g:
    print(item)
    pass
print(l,g)
"""
#
# a= [j+1 for j in range(10) ]
# print(a,type(a))

b=(l+1 for l in range(10))

print(list(b))
print(list(b))