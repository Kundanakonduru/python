k="MadaM"
s=""
n=len(k)
for i in range(n-1,-1,-1):
    s+=k[i]
print(s)
if s==k:
      print("Palindrome")

else:
    print("Not palindrome")
