# Object Oriented Programming

# class Dog:
#     def __init__(self,name,age, breed, color):
#         self.name =name
#         self.age =age
#         self.breed = breed
#         self.color = color

#     def run(self):
#         print(self.name + " is running")

#     def bark (self):
#         print(self.name + " says woof woof!")
#     def sit(self):
#         print(self.name, "is sitting!")
#     def fetch (self):
#         print(self.name + "is fetching the stick")



# sire_dog = Dog(name="lucky",breed= "german shepard", color ="brown", age= "6 months")

# sire_dog.sit()

# Inheritance

# class Animal :
#     def __init__ (self,name):
#         self.name = name

#     def speak(self):
#         print("Animal default sound")
# # subclass     
# class cat (Animal):
#     def speak(self):
#         print(self.name, " is meowing!")


# cat = cat("frodo")
# cat.speak()


# # encapsulation
# class bankAccount:
#     def __init__(self,initial_balance):
#         self.__balance = initial_balance

#     def deposit(self,amount):
#         self.__balance += amount
#         print("Deposited ", amount, "New balance is ", self.__balance)


# class bank(bankAccount):
#     def sire(self):
#         print(self.__balance)



# class Animal :
#     def __init__ (self,name):
#         self.name = name
        
#     def speak(self):
#         print("Animal default sound")
# # subclass     
# class cat (Animal):
#     def speak(self):
#         print("meow!")

# cat = cat("frodo")
# cat.speak()


# polymorphism
# class Car:
#     def __init__(self, name, model,color):
#         self.name=name
#         self.model = model
#         self.color = color

#     def top_speed(self):
#         print(self.name, " has Top speed of 200mph")
        


# class BMW(Car):
#     def AirConditional(self):
#         print("this car has AC")


#     # def top_speed(self):
#         # print(self.name , " has max speed of 350 mph")



# vehicle = BMW(name="BMW", model="2016", color = "RED")
# vehicle.top_speed()



# dictionary {}

# my_dict = {"girl": "Zikabereyi",
#            "boy": "Siyishire"}
# print(my_dict)



# students_marks = {'John': 65,'shawn':73,'eze':23}


# coding_skul = {"beginners":["henry", "michael", "Joy"],
#                "Intermdiate":["mary", "blessing","Joseph"], 
#                "Professionals": ["zika", "shire", "lucas"]}
# # print(coding_skul.get("beginners"))
# print(coding_skul.values())


# password = ''
# while password != "random":
#     password = input ("provide a password ")
# print("welcome!")

# class Citizens:
#     def __init__(self,name,age, state):
#         self.name = name
#         self.age = age
#         self.state = state


# class eligibiliy(Citizens):
#     def can_vote(self):
#         if self.age >= 16:
#             print (f"{self.name}  who is  {self.age}  from the state of  {self.state}  can vote.")
#         else:
#             yr_rem = 16-self.age
#             print (f"you are not eligible to vote, try again in   {yr_rem} years time")

# voter = eligibiliy(name= "zika", age= 10, state = "colorado")
# voter.can_vote()

# cousins= ["osamudian",'osato', 'odion']
# guess = ""
# while guess not in cousins:
#     guess = str(input("provide a cousin name "))
# print("correct!!")

# str1 = "Application"
# str2 = str1.replace("a","A")
# print (str2)

i = 0 #initilaize 
# while i < 3: # true
#     print("hello")
#     i +=1

# j=1
# while j <= 5:
#     print(j)
#     j= j+1