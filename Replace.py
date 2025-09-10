s = input("Enter a String: ")
first_char = s[0]
modified = first_char + s[1:].replace(first_char,"$")
print("Modified String:",modified)