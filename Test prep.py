username = input("What is your name?")
print("Hello," + username + "!")

# or
# name = "jacqueline"
print("Hello," + name + "!")

text = "apple"
#String
number = 10
#Integer
decimal = -10.3
#Float
has_money = True
#Booleam
coordinates = (2.5, 1.5)
names = ["Jacqueline", "is"]
#List
unique = {1,2,3,4,4,5,6}
print(unique)
#Doesn't print duplicates
users = {"Bob": 1, "James": 2}
#Dictionary, Holds key value pairs in a list-like structure

#Type constructer to change a data type into another
number = "100"
#doesn't add with 10 in print(10 + number)
#Only works if it is an integer or float inside the string
print(10 + int(number))
print(float("100.0"))
#Changes string 100 into float

age: int = 10
name: str = "Bob"
# :10 is an annotation to tell our code age is an integer which helps us determine errors in future code

#F-Strings
print("Name:" + name + ", Age:" + str(age))

