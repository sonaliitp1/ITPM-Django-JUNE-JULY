# # wap to print factorial of given number 
# # no argument no return 
# def fact():
#     num = 5 
#     f=1 
#     for i in range(1,num+1):
#         f = f * i
#     print(f"Factorial :- {f}")
# fact()

# # with argument no return type 
# num = 5
# def fact(num):
#     f=1 
#     for i in range(1,num+1):
#         f = f * i
#     print(f"Factorial :- {f}")
# fact(num)

# # no argument but return 

# def fact():
#     num=5
#     f=1 
#     for i in range(1,num+1):
#         f = f * i
#     return f
    

# result = fact() or  print(fact())
# print(result)

# # with argument with return 
# num =5
# def fact(num):
#     f=1 
#     for i in range(1,num+1):
#         f = f * i
#     return f
# print(fact(num))

# Greatest of 3 nos using function -- with argument with return

def greatest(a,b,c):

    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

print(greatest(10,20,30))

# print max number from given list using function 
# with argument no return 
list1 =[23,34,56,78,12,90,45]

def max_number(l):
    max = 0 
    for i in l:
        if i > max :
            max = i 
    print(f"Max Number :- {max}")
max_number(list1)

# Print square and cube of numbers upto given range
# square -- only even numbers 
# cube == only odd numbers 
# no return no argument

def sqcube():
    n1 = 20
    n2 = 50
    for i in range(n1,n2+1):
        if i%2==0:
            print(i**2)
        else:
            print(i**3)
sqcube()








