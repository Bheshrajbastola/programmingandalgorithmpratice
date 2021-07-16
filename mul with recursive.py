def mul(num):
    if num==1:
        return num
    else:
        return 3+mul(num-1)
for i in range(1,11):
    print(f"3*{i}={mul(i)}")
     #print(i)

