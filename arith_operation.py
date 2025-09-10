a=int(input("Enter First integer: "))
b=int(input("Enter Second integer: "))

print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("multiplication: ",a*b)

if b!=0:
    print("Division",a/b)
    print("Modulus",a%b)
else:
    print("Division and Modulus not possible (b=0)")