# Multiplication table (from 1 to 10) in Python


# To take input from the user
num = int(input("Display multiplication table of given number: "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 20):
   print(num, '*' , i, '*', num)