n = input("Enter a string: ")
if len(n)>1:
    new_n = n[-1] + n[1:-1] +n[0]
else:
    new_n = n
print("Modified String:",new_n)