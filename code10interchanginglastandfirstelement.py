# interchange the first and last element of the list. 
a = [1, 2 , 3, 4]
print(a)
# b = a[0]
# c = a[-1]
# a[0] = c
# a[-1] = b
# print(a)

b = a[0]
a[0] = a[-1]
a[-1] = b
print(a)

