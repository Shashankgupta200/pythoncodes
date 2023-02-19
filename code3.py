is_male = True
is_tall = True
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a male but not tall")
else:
    print("you are neither male nor tall")
num1 = float(input("Enter the first number: "))     #float is directy used here so that the input gets converted to integer value instantly.
opp = input("Enter operator: ")                     
num2 = float(input("Enter the second number: "))    #conversion was needed because by default the input is taken as string
if opp == "+":
    print(num1 + num2)
elif opp=="-":
    print(num1-num2)
elif opp=="/":
    print(num1/num2)
elif opp=="*":
    print(num1*num2)
else:
    print("Invalid operator!!")
