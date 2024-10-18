a = int(input("Enter your age: "))
print("your age is:", a)
# Conditional operators
# >, <, >=,<=,==, !=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
if(a>18):
    print("You can drive")
    print("Yes")

else:
    print("You can drive")    
    print("No")
    print("Yay!")

num = 18 
if(num< 0):
    print("Number is negative.")
elif(num > 0):
    if (num <= 10):
       print("Number is between 11-20")
    else:
        print("Number is greater than 20") 

else:
    print("Number is zero")