# from selenium import webdriver
# """Write a python program to print based on below rule
# Range of number 1 - 100
# if a number is divisible by 3, print "Pine"
# if a number is divisible by 5, print "Apple"
# if a number is divisible by both 3 and 5, print "Pineapple"""
#
# def numb(a):
#
#     if(a%3 and a%5)==0:
#         print("Pineapple")
#     elif (a % 3 == 0):
#         print("Pine")
#     elif (a % 5 == 0):
#         print("Apple")
# numb(30)
#
# b=[10,30,79,58,70]
# print((len(b)))
# b2=0
# c=[]
# for i in range(len(b)):
#     for j in range(len(b)):
#         if (b[i]>b[j]):
#             b2+=1
#         if (b2==4):
#             c.append(b[i])
#     b2=0
# print(c)

l = [item + 1 for item in range(10)]
for item in l:
   # print(item)
   pass
g = (item + 1 for item in range(10))
for item in g:
    print(item)
    pass
print(l,g)

a={"a":"harsh","b":"bhawsar"}
for i in a.values():
    print(i)

add = lambda x,y: x + y
print(add(5, 3))

a= lambda x:x+5
print(a(100))

a=[1,2,3,4,5,6,7]
b= list(filter(lambda x:x%2==0,a))
print(b)

c=[10,20,30,40,50]
c1=list(map(lambda z:z*2,c))

print(c1)