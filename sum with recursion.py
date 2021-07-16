def sum(num):
    if num==1:
        return 1
    else:
        return (num+sum(num-1))
num=int(input("enter a number : "))
a=sum(num)
print(a)

