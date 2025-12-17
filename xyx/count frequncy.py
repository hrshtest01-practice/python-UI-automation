a=['a','b','a','c','z','x','x','j']
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
print("cat"=="act")