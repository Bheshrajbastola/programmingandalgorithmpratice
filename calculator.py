def add (num1 , num2):
    """this is first docstring"""
    return (num1+num2)
def subtract (num1 , num2):
    return (num1-num2)
def divide (num1 , num2):
    return (num1/num2)
def multiply (num1 , num2):
    return (num1*num2)
def modolus (num1 , num2):
    return (num1%num2)
def floordivide (num1,num2):
    return (num1//num2)

print("select the operation\n ")
"1. Add\n" \
"2. Subtract\n" \
"3. Multiply\n" \
"4. Divide\n" \
"5. Modolous\n"

select =int(input("select number from 1,2,3,4,5,6 : "))
num1=int(input("enter a first number : "))
num2=int(input("enter the second number : "))



if select == 1:
    print(num1, "+", num2, "=",
          add(num1 , num2))

elif select == 2:
    print(num1, "-", num2, "=",
          subtract(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=",
          multiply(num1, num2))
elif select == 4:
    print(num1, "/", num2, "=",
          divide(num1, num2))
elif select == 5:
    print(num1, "%", num2, "=",
          modolus(num1, num2))
elif select == 6:
    print(num1,"//",num2,"=",
          modolus(num1,num2))

else:
    print("entered number is invalid")







