try:
    number = int(input("Enter a number: "))
    print(number)
    value= 10/0
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cant divide by zero")
# except:                                   #only except apply for all the errors
#     print("Invalid error!!")              #to take only specified errors type of error must be mentioned