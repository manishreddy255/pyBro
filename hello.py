

# now This is python and we will start

# now we have to print hello

# print("hello")


# variable = a container for a value. Behaves as a container for some
#     value

# name = "Bro"
# print("hello" + name)
# print(type(name))

# you can join variable as long as they are of same data type

# name = "manish"
# listing = "hey this is listing"
# print(name + listing)
# you can do this

# now we will use another one with other data type
# dating = 78
# print(name + dating)
# you can't do this

# you can't concatenate two things of differeent type in python
# you can only do it after changing the type of the variable
# with type casting
# in this the data of one type is changed to another type
# age = 34
# print("hey how are you my age is :" + str(age))

#This is what you call a float data type

# height = 237.79
# print(height)
# print(type(height))
# print("your height is : " + str(height))

#boolean data type

# human = True
# animal = False
#
# print(animal)
# print(type(animal))
# print("Ar eyou a human ?: " + str(animal))

#multiple assignment in python
# assigning multiple variables at a tim

# name = "manish"
# age = 25
# attractive = True
# print(name)
# print(attractive)
# print(age)

# name, age, attractive = "manish", 78, True
#
# print(name, age, attractive)
#
# spongeBob = hermit = bunny = 78
#
# print(spongeBob)
# print(hermit)
# print(bunny)

#useful methods for strings

name = 'manish'

# print(len(name))
# print(name.find("m"))
# print(name.capitalize()) # emits copy with capitalized string
# print(name.upper())
# print(name.lower())
# print(name.isdigit()) it can be used to know if the thing is a string or not
# print(name.isalpha()) if the string contain all strings
# print(name.count("a"))
# print(name.replace('i', 'ki'))
# print(name*78) with this you can print it multiple times

#********** Type casting ****************
# it is ability to convert one data type to another
# x = 1
# y = 2.0
# z = "ama"
# k = "89"
#
# # int(y) # this just emits something and doesn't change anything
# y = int(y)
# print(x, y, z*3)
# k = int(k)
# print(k*3)
# print(type(x))
# print(type(y))
# print(type(z))

# ************ input accepting and performing op's **************

# doing = input("what are you doing ?")
# print("so you are " + doing)
#
# #important point whenever you give something in input
# # it is always a string and you can only type cast it to something
# #else
#
# age = int(input("hey what is your age ?: "))
# print(age, type(age))
# print(" So your age is " + str(age) + " then you can  who ever you want")


# import math
#
# pi = 3.14
# print(round(pi))
# print(math.ceil(pi)) # ceil rounds it to upper
# print(math.floor(pi)) # floor rounds it down
# print(abs(pi)) #it will give you absolute value of
# how much far it is from the 0
# print(pow(34, 6))
# print(pow(3,2))
# print(math.sqrt(420))
# x, y , z = 1, 2, 3
# print(max(x, y, z))
# same with min function

#string slicing
# creating a substring by extracting elements from another string
# indexing[] [start:stop:step]
# step is how many you wanna skip
# name = "manish Reddy"
# first_name = name[0:2]
# first_name = name[:2]
# last_name = name[7:]
# funky_name = name[::2]
# print(first_name)
# print(last_name)
# print(funky_name)
# # reverse the string in python
# reversed_name = name[::-1]
# print(reversed_name)

# now slice function to create a slice object

# website = "http://google.com"
# website2 = "http://wikipedia.com"
#in python we have positive and negative index
#for everyting so we can't predict the length of domain
# so we use negative index that is -4 to get results
# slice = slice(7,-4)
# #now we have slice object
# print(slice)
# print(website[slice])
# print(website2[slice]"
# print(website.split(":"))
#*******decision making Structures or if statements ****************
#if statement  is a block of code that will execute if it's
#condition is true
# age = int(input("How old are you? : "))
#
# if age >= 21 | age <= 99:
#     print("you are eligible to drink ")
# elif age == 100:
#     print("you have drank for so many years, so just cut on alcohol")
# elif age < 0:
#     print("you mother is eligible to drink")
# else:
#     print("you are not eligible to drink")

# in python we have indentations and don't have brackets
#so and of or and and operations

# logical operators in python
# they are "and" and "or" operators

# temp = int(input("what is the temperature outside: "))
#
# if not(temp >= 0 and temp <= 30):
#     print("it's ideal temperature")
# elif not(temp <30 or temp > 30):
#     print("it's going up macha")
#for 'and' if both of them are true then only the given statement is true
#for or if only one statement is true you can get true value
# there is also a not operator with which you can
# turn a true to false
# false to true
# so by using this condition we reversed the props


#**** while loop in python ************
# i = 1
# while i == 1:
#     print("hey how are you")

# name = ""
#
# while len(name) == 0:
#     name = input("Enter your name: ")
#
# print("hello " + name)

# name = None
#
# while not name:
#     name = input("hey what is your name: ")
#
# print("Hello " + name)

#********** For Loop *************
# for i in range(10):
#     print(i+1)

# 50 is inclusive and 100 in not inclusive
# for i in range(50, 100):
#     print(i)

# for i in range(50, 100+1, 2):
#     print(i)
# it increments 2 at a time

# for i in "bro code":
#     print(i)

# import  time
#
# for seconds in range(10, 0,-1):
#     print(seconds)
#     time.sleep(1) # it will sleep for 1 second
#
# print("happy new year")





























