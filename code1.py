print('Hello, world!')
phrase = "this is my first code"
print(phrase.upper())      #upper fuction makes the string in uppercase
print(phrase.isupper())     #isupper function gives true and false as output.
print(phrase.upper().isupper())     #we can use functions like this consecutively.
print(len(phrase))      #gives the length of the string
print(phrase[0])        #gives the nth position value of the string
print(phrase.index("i"))        #gives the index of the given character
print(phrase.replace("code", "program"))        #replaces the given word with another word
num = 7
print(num)
print(str(num) + " is my favourite number")     #convet the number into a string. if not converted then error will be thrown.
print(3+5)      #you can directly do arithmatic operation in print statement
print(pow(2, 5))
print(max(5, 6))
from math import *      #imports complex math functions
print(round(5.33))
print(sqrt(64))
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + " you are " + age + " years old")
friends = ["tom" , "jerry", "mike", "bob", "bob"]
print(friends[1:])      #intializes and run till the array ends
print(friends[1:2])     #we can also decide upto where it should show.
lucky = [1, 2, 8, 4]
friends.extend(lucky)       #extend the list by adding another array to the end of the list.
print(friends)
friends.append("cody")        #append- add something at the end
print(friends)
friends.insert(1, "larry")      #insert values at random numbers
print(friends)
friends.remove("tom")
print(friends)
friends.pop()
print(friends)
# friends.clear()
# print(friends)
print(friends.index("jerry"))
print(friends.count("bob"))
lucky.sort()
print(lucky)
lucky.reverse()
print(lucky)
friends2 = friends
print(friends2)
