l=[100,20,30,0,4,690,50,900]
n=len(l)
j=l[0]

for i in range(n):
    if l[i] > j:
        j = l[i]

print(j)
