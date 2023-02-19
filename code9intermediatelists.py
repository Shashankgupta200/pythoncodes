mylist = ["shashank", "gupta", "python"]
print(mylist)
print(mylist[-2])       # here -2 indicates the 2nd last element from the end of the list
mylist.append("programmer")     #adds content at the end of the lists.
print(mylist)
mylist.insert(2, "gamer")
print(mylist)
mylist2 = list()
print(mylist2)          #creates an empty list for future inputs
item = mylist.pop()     #takes out(delete) the last element of the list
print(item)              
mylist.remove("gamer")  #takes out specific element from the list
print(mylist)
mylist3 = [2, 3, 9, 4, -6, -1, 0]
new_list = sorted(mylist3)      #if we dont want our original list to be sorted then we can assign the new name to the list and use sorted function 
print(new_list)
print(mylist3)
mylist3.sort()             #sorts the list in ascending order.
print(mylist3)
mylist4 = [0] * 5       #this will be equal to [0, 0, 0, 0, 0]
print(mylist4)
mylist5= [1,2,3,4,5]
new_list2= mylist4 + mylist5        #this will add the two list and give the output
print(new_list2)    
a= mylist5[1:3]             #this will select a particular range of values from the list but the last value will be ignored. if we
                            #dont specify the last index then it will print till the end of the list.
print(a)    
b= mylist5[::2]             #this is called step index where it takes every 2nd element from the list similarly if we take 1 in place of 2 then it
                            #will print all the element of the list.
print(b)
c= mylist5[::-1]            ###reverses the list shortcut method 
print(c)
mylist5_cpy = mylist5.copy()    #it will make a copy of the original list without changing anything in the original list.
                                #if we only write mylist5_cpy = mylist5 then the changes made in the copy list will be shown in the original list.
mylist5_cpy.append(6)           #adding value to the copied list which will not affect the original list.
print(mylist5_cpy)