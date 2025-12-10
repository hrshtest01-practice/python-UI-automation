a,b,c="silent","silett",0
if (len(a)==len(b)):
    for i in range(len(a)):
        if a[i] in b:
            c+=1
        else:
            print("Not a anagram")
            break
        if (c == len(a)):
            print("string is anagram")
else:
    print("string is not anagram")
print(sorted(a))
