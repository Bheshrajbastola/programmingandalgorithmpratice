def mul(num,i):
    if i>10:
        return
    print(num,"*",i,"=",num*i)
    return mul (num,i+1)
num=int(input("enter a number ;"))
mul(num,1)
