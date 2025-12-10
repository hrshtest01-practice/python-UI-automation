# from locust.util.exception_handler import retry
# def a():
#     strs = ["c","acc","ccc"]
#     f1=""
#     b=strs[0]
#     count =0
#     for i in range(len(b)):
#         a= b[0:i+1]
#         print(a)
#         for j in strs:
#             j1 = j[0:i+1]
#             if a in j1:
#                 count+=1
#         if count == len(strs):
#             f1=a
#             count=0
#         else:
#             print(f1,"mid")
#             return f1
#     print(f1,"last")
#     return f1
# a()
#
a=[1,2,3,4,5,6]
a.insert(0,0)
print(a)
for i in a:
    if 0 in a:
        print('yes')
        exit()
    else:
        ("no")