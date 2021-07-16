
def fibonnaic(num):
    if num<=1:
        return num
    else:
        return fibonnaic(num-1)+fibonnaic(num-2)
num=int(input("enter a number : "))
for i in range(num):
  print(fibonnaic(i))

