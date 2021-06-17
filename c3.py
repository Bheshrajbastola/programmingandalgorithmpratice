''' If name is less than 3 characters long- name must be at least 3 characters
  otherwise if it's more than 50 characters - name must be maximum of 50 characters
  otherwise - name looks good!
'''
a =input("enter any name with at least three character :")
if len(a)<3:
    print("it is less than three character")
elif len(a)>50:
    print("name must not be 50 character")
else:
    print("Name looks good")