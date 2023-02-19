month_conversion={          #here a dictionary is being made and each value should show unique name
    "Jan":"January",        #these are written so that when short form are written then it automatically gets converted to longer form
    "feb":"february",
    "mar":"march"
}
print(month_conversion["feb"])
print(month_conversion.get("mar"))  #.get was used so that if any invalid key is passed then it will just show none
i=1             #initiates i
while i<=10:    #simple while loop
    print(i)
    i+=1
print("Done with the loop!!")
for letter in "shashank":
    print(letter)
friends=["tom", "jerry", "bob"]
for index in range(len(friends)):
    print(friends[index])

def power(number, pow):         #function made to calculate the power of a number
    result=1
    for i in range(pow):
       result=result*number
    return result
print(power(3, 4))              #function call


#check if a string contains a vowel
name = input("Enter a string: ")
for i in name:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        print("The word " + name + " contains vowels")
        break

