# g=[2,3,4,5]
# def func():
#     print(sum(g))
# func()

# def func(a,b):
#     return a+b
# print(func(1,2))

# def func(a=1,b=2):
#     return a+b
# print(func())


# def func(a,b=2,c=3):
#     return a+b+c
# print(func(1))
# print(func(1,b=4,c=5))


# def func(*a,**b):
#     print(a)
#     print(b)
# print(func(1,2,3,name= "Ubam",age="33"))


# a=0
# def func():
#     global a
#     a=3
#     b=2
#     return a+b
# c=a+2
# print(func())

# def func(a,b):
#     return a+b
# print(func(1,2))
# d=int(input("число:"))
# def func():
#     if d%100==0 or d%4==0 or d%400==0:
#         return("высококосный")
#     if d%100!=0 or d%4!=0 or d%400!=0:
#         return("простой")
# print(func())


d=(6,5,8,9,3,2,2,2)
def func(d):
    f=0
    for i in d:
        if i!=int(i):
            f+=1
    if f>0:
        print(d)
    else:
         print(sorted(d))
print(func(d))
