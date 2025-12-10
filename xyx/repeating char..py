I= "harsah"
# Output: "u"
# Input: "aabbcc"
# Output: None

for i in range(len(I)):
    x = 0
    for j in range(len(I)):
        if (I[i]==I[j]):
            x+=1
            if x>1:
                break
    if x==1:
        print(I[i])
        break
    if (i == len(I)-1):
        print('none')


