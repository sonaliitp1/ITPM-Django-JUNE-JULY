# # wap to check the given number is prime or not using function 

# def check_prime(n):  # 11
#     f=0
#     for i in range(2,n):
#         if n%i==0:
#             print("Number is not prime")
#             f=1
#             break 
#     if f==0:
#         print("Number is prime")
    
# num = int(input("Enter any nunber"))
# check_prime(num)

# # ATM Withdrawl
# # Ask the user to enter the balance and withdrwal amount. if withdrawl amount smaller than balance ,then deduct it and print remaining balance else print "Insufficient balance"



def show_list(*numbers):
    for i in numbers:
        print(i)
show_list(12,23,45,67,99)


def show_dict(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}={value}")
show_dict(name="abc",age=23,city="Pune")

def show_info(name="ABC"):
    print(name)

show_info()


str = "Welcometoitp"

# create character count dictionary 

# dict1 ={'W':1,'e':2 ...}

str ="welcome"
print(str.count('e'))








