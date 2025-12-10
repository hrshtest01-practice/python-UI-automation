#reverse a string
# a="harsh bhawsar"
#
# b=a[::-1]
# print(b)

# check string palindrome
#
# a= "saras"
# b= a[::-1]
# print(a==b)

#count vowels and consonents
# a= "harsh bhawsariiiiA"
# x="aeiou+AEIOU"
# v,w=0,0
# for i in a:
#     if i in x:
#         v+=1
#     else:
#         w+=1
# print(v,w)


# #Find duplicate characters
# a= "harsh bhaswas harsh bhawsar harsh bhawsar"
# x = {}
# for i in a:
#     if i in x:
#         x[i]+=1
#     else:
#         x[i]=1
# print(x,type(x))

# string is anagram or not
a="harsh"
b="ahhrs"
a1=a.split(',')
b1=b.split(',')
print(a1,b1)
print(a1==b1)