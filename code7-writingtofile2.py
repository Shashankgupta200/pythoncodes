file2 = open("demo2.txt", "w")                      #when "w" is added then whole file gets deleted and content is overriden
file2.write("\nNew content added to the file. ")    #if we give wrong name in open function then a new file is created
file2.close()                       

####we can also write a html file inside the write function and a new html file will be created
