# area of rectangle

a=int(input("Give the value for length:"))
b=int(input("Give the value for breath:"))
if(a>b):
    result = a*b
    print("the area of rectangle is:",result)
elif(a=b):
    result = a*a
    print("the area of square:",result)
else:
    print("there is no breath is greater than legth")

print("finally it is printed successfully")

