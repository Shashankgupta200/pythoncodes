file = open("demo.txt", "r")       #this function opens a file and "r" is used so that the file can be open in read mode. "w" is used to open the file in write
# print(file.readlines())              #to read the content line by line
for i in file.readlines():              #we can use for loop like this to read a file.
    print(i)

# print(file.readline())
# print(file.readline())
# print(file.read())                  #print all the content in the file
# print(file.readable())              #to check if the file is readable or not.
file.close() 