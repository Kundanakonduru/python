#using while loop
l = [44, 88, 32, 3, 1, 67, 93, 55, 32, 21]

j = l[0]   # assume first element is largest
i = 1

while i < len(l):
    if l[i] > j:
        j = l[i]
    i += 1

print("Largest number:", j)

#using for loop
l=[44,88,32,3,1,67,93,55,32,21]
j=1
for i in l:
    if i>j:
        num=i
        j=i
    
print("Largest number:",j)
