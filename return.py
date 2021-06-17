''''Add- no parameter no return statement
Sub- parameter and no return statement
Mul- no-paramter and return statement

Div- parameter and return statement'''
def add():
 c=int(input("enter a number:"))
 d=int(input("enter a number:"))
 a=c+d
 print(a)

def sub(a,b):
   c=a-b
   print(c)
   sub(5,2)

def mul():
    c = int(input("enter a number:"))
    d = int(input("enter a number:"))
    a=c*d
    print(c)

def div(a,b):
    c=a/b
    return c
div(6,3)