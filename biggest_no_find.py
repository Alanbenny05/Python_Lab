a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))

biggest=a
if b>biggest:
    biggest=b
if c>biggest:
    biggest=c

print("Biggest number is:",biggest)