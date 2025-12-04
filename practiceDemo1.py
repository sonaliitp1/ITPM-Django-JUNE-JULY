# fruits = ["Apple","Banana","Mango","Kiwi","Orange"]
# # replace fruit name with another name using index
# # fruits[2] = "Cherry"
# # print(fruits)

# # print length of fruits list 
# print(f"Length of Fruits :- {len(fruits)}")

# # Print all fruits using range
# for i in range(0,len(fruits)):
#     print(fruits[i])

# # Another way to print all fruits without range
# for i in fruits:
#     print(i)

# # print all fruits which fruit length >=5

# for i in fruits:
#     if len(i) >=5:
#         print(i)

# numbers =[23,45,66,78,90,33,12,27,44]
# # print only even numbers from  numbers list 

# for i in numbers:
#     if i%2 == 0:
#         print(i)

# # get even numbers and add into even_list and vice versa 

# even_list =[]
# odd_list =[]

# for i in numbers:
#     if i%2==0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print(f"Even Numbers List :- {even_list}")
# print(f"Odd Numbers List :- {odd_list}")

# # print numbers in alternate order 

# print(numbers[0:len(numbers):2])

# # print greatest number from numbers list without using inbuilt() method 
# [23,45,66,78,90,33,12,27,44]

# max = numbers[0]  
# for i in numbers: 
#     if i > max:         
#         max = i   
# print(f"Max Number :- {max}")

# # Ask the user to enter any fruit name  and check if it is present in fruits list or not if it is present then print "kiwi is present at 4 location" otherwise "kiwi is not present"

print("hello")

# fname = input("Enter fruit name")
# f = 0
# for i in range(0,len(fruits)):
#     if fruits[i] == fname:
#         print(f"{fname} is present at {i} location")
#         f=1
#         break
    
# if f==0:
#     print(f"{fname} is not present in given list")

str1="banana"
dict1={}
for i in str1:
    dict1.update({i:str1.count(i)})
print(dict1)
    
marks = {"Ali": 85, "Sara": 92, "Zain": 78,"ABC":100,"xyz":120}
max =0
name =""
for key,value in marks.items():

    if value > max:
        max=value
        name=key
print(f"{name}:{max}")

students = [
    {"name": "Alice", "age": 20, "major": "Math","m1":23,"m2":56},
    {"name": "Bob", "age": 22, "major": "Physics","m1":23,"m2":56},
    {"name": "Charlie", "age": 21, "major": "CS","m1":23,"m2":56}
]

for i in students:
    sum=0
    for key,value in i.items():
        if key =="m1" or key=="m2" or key=="m3":
            sum+=value
    i.update({"total":sum})
    print(i)


