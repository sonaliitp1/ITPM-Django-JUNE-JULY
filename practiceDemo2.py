fruits ={
    "apple":200,
    "mango":500,
    "cherry":340,
    "orange":100,
    "banana":50
}

# print(fruits)

# #iterate Dictionary 
# for key,value in fruits.items():
#     print(f"{key} price :- {value}")


# Addition of all fruits prices
# sum=0
# for key,value in fruits.items():
#     sum+=value
# print(f"Sum of all fruits prices:- {sum} ")

#Ask the user to enter key and print corrosponding value of the key

# k = input("Enter any key")
# for key,value in fruits.items():
#     if key == k:
#         print(f"{key}:-{value}")
#         break
# else:
#     print("Key not found")

# print highest price fruit name

max=0
for key,value in fruits.items():
    if value > max:
        max = value
        k = key
print(f"Highest Price :-{k}:- {max}")
    
# List of dictionary

students =[
    {
        "rno":1,"name":"Rohit","m1":34,"m2":78,"m3":99
    },
    {
        "rno":2,"name":"Atharva","m1":77,"m2":56,"m3":100
    },
    {
        "rno":3,"name":"Riya","m1":74,"m2":66,"m3":89
    },
    {
        "rno":4,"name":"Sagar","m1":63,"m2":92,"m3":43
    },
    {
        "rno":5,"name":"Yash","m1":52,"m2":49,"m3":91
    }
]

for i in students:
    for key,value in i.items():
        print(f"{key} :- {value}")
    print()
        
    
# Ask user to enter rno and print corrosponding dictionary details

r = int(input("Enter Roll Number"))
f=0
for i in students:
    for key,value in i.items():
        if value == r:
            print(i)
            f=1
if f==0:
    print("Roll number not found")


# print all subjects total of each student

for i in students:
    sum=0
    for key,value in i.items():
        if key =="m1" or key=="m2" or key=="m3":
            sum+=value

    i.update({"totalmarks":sum})
    print(i)


