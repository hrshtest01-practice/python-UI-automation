list1=[1,[2,3],4,[5,6],9,[8,9],10]
l=[]
def aa(b):
    for i in range(len(b)):
        if type(b[i])==int:
            l.append(b[i])
        else:
            aa(b[i])
aa(list1)
print(l.sort(),l)
