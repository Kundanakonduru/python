x = input("Enter password:")
s = "~!@#$%^&*()_+?"

special = False
number = False

for i in x:
    if i in s:
        special = True
    if i.isdigit():
        number = True

if len(x) >= 8 and special and number:
    print("Valid")
else:
    print("Invalid")
