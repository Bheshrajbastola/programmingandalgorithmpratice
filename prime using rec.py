'''def prime(num,i=2):
    if (num<=2):
        return "prime"
    else:
        return prime(num,i+1)
num=int(input("enter a nuber :"))
prime(num,i=2)

'''
def check(n, div=0):
    if div is 0:
        div = n - 1


        if n % div == 0:
            print("Number not prime")
            return False
        else:
            return check(n, div - 1)
    else:
        print("Number is prime")
        return 'True'


n = int(input("Enter number: "))
check(n)

