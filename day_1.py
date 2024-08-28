# '' 
# ""
# '''siyishire said,"that he is not hungry".'''  # this is what siyishire said
# "Ade goes to school." 
# string 
# str
# 1 
# integer
# int
# # "1"
# #
# # 
# 1.6783876423
# True or False

# [] # list
# () # tuple
# {} #dictionary 

# # uses of python
# # web development
# # data analysis
# # game develop
# # web scrapping

# ####data types
# # str
# # int
# # float
# # boolean
# # list
# # tuple
# # dictionary


# # variable 
# age = 80
# name = "zika"


# print("siyishire said he is not hungry")
# print ("Hello, world !")

# a = "zika"
# vehicle = "Toyota"
# b= 10

# print("a")


# name = input("What is your name ? ")
# print (name)
# print ("name")

# print ("hello",name, '!')
# print ("Hello " + name +'!')
# + is  concatenation 
# variable name can be alpha numeric (age1, b1)
# variable can start with underscore (_A_)


# x,y,z="ade"
# print(z,y,x)


# a = 2
# b = 3

# print(a - b)

# Lists [] squared bracket
# list are mutable
fruits = ['apple', 'orange', 'pineapple', 'mango', 'watermelon','guava']
# # .append1 is used to add item to a list
# # variable_name.append("element to add")
# print(fruits)
# fruits.append("avocado")
# print (fruits)

# index is the position of an item in a list
# print(fruits[4])
# # slicing :
# print(fruits[2:3])
# removing element from a element
# .pop(), del ,
# fruits.pop(3)
# print(fruits)

# del fruits[0:2]
# print(fruits)

# fruits.clear()

# fruits.sort(reverse=True)
# print(fruits)

# Tuples
# fruit = ("pineapple","tangerine","orange")
# a = len(fruit)
# print(a)
# print(fruit[-1])

# control flow
# Age = int(input("How old are you"))
# if  Age >= 41:
#     print("you are an elder")
# elif Age >=18:
#     print("You are an adult")
# elif Age  >= 9:
#     print("Your are an Adoslescent")
# else:
#     print("you are a baby")



# loop 
# for and while
# for i in fruits:
#     print(i)
# for i in range(1,13):
#     for j in range(1,13):
#         result = j * i
#         print(i , " *", j ,"=" ,result)

# print(4 % 2)
# write a program that will take an input of a number and determine if a number is an odd or even number. %
# write a program that will take an input of a number and determine if a number is a prime number.

# s1 = "python"
# s2 = s1[::-1]
# print(s2)
# s3 = ''.join(reversed(s1))

# print(s3==s2)

# if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True




# while loop
# i = 0
# while i < 9:
#     print("hello", i)
#     i =i+1
# x= 20
# y =10
# while x < 50 and y <20:
#     x += 1
#     y +=1
#     print(x ,y )


# def greet(args):
#     print("hello", args)
# greet("siyishire")

# def add(a,b):
#     result = int(a) +int(b)
#     return result
# # print(add(3,5))

# def add(a=0,b=0,c=0):
#     result = a+b+c
#     return result

# print (add())


# chores = 30
# paper = 20
# expenses = 10

# def savings(chores,paper, expenses):
#     total_money_earned = chores +paper
#     total_expenses = expenses
#     savings_per_week = total_money_earned- total_expenses
#     savings_per_year =savings_per_week * 52
#     return savings_per_year


# result = savings(chores= 100, paper=50,expenses=30)

# print(result)

# Modules
# import random
# random
# print(random.choice([1,2,34,6,65]))

# def greet(name):
#     print ("Hello", name)
# greet("bob")

# def addition(a,b):
#     result = a+b
#     print (result)


# addition(4,5)

# import my_module
# from my_module import subtraction
# # my_module.subtraction(8,6)
# a = subtraction(7,6)
# # print(a)


# from turtle import Turtle, Screen


# t = Turtle()
# t.shape("turtle")

# for i in range (6):
#     t.forward(50)
#     t.left(60)
# t.forward(50)
# t.left(90)
# t.fd(50)
# t.left (90)
# t.fd(50)
# import random
# t.circle(10)
# colors = ["cornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
# def shapes (num_sides):
#     for i in range (num_sides):
#         t.forward(50)
#         t.color(random.choice(colors))
#         t.left(360/num_sides)


# for i in range (4,10):
#     shapes(i)

# screen = Screen()
# screen.exitonclick()


# A sum of money amounts to Rs. 28,000 in 2 years at 20 % simple interest per annum. Find the sum.
#2. What would be the annual interest accrued on a deposit of Rs. 10,000 in a bank that pays a 4 % per annum rate of simple interest?
#3. Joseph buys a home valued at $200,000 and pays 5% interest per year on the home. Calculate the interest.


# Amount = Principal + interest 

# Amount = 28,0000
# rate = 0.2
# Principal= 
# time = 2
# interes =


# S.I = P* R* t


# import my_module 

# # interest = my_module.Simple_Interest(10000,0.04,1)
# # print (interest)


# from my_module import Simple_Interest
# interest = Simple_Interest(200000,0.05,1)
# print (interest)








# ###################### Reading from  & writing to  a file###############################


# file = open("example.txt",'w')
# content =file.write("Hello world!")
# # print(content)
# file.close()
# path
# absolute
# # relative
# file = open(r"C:\Users\adeso\OneDrive\Desktop\test\example.txt","r")
# content = file.read()
# print(content)
# file = open(r"C:\Users\adeso\OneDrive\Desktop\Untitled.ipynb","r")
# content = file.read()
# print(content)
# file.close()
 
# from turtle import Turtle
# from random import random

# t = Turtle()
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)

# t.screen.mainloop()





# def checking (num): 
#     j=0
#     for i in num:
#         if i >j:
#             j =i
#         else:
#             pass
#     return j

# num =[6,12,87,92,180,6]
# highest = checking(num)
# print (highest)