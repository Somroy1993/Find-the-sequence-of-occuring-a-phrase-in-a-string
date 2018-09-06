c=0 #count
s=input("input the string")
for i in range(len(s)):
    if s[i]=='b' and s[i+1]=='o' and s[i+2]=='b':
        c+=1
print(c) #returns number time bob is repeated
