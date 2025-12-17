#nested list
lst = [1, [2, 3], [4, [5, 6]], 7]
b=[]
def a(x):
    for i in x:
        if type(i)==int:
            b.append(i)
        else:
            a(i)
a(lst)
print(b)
