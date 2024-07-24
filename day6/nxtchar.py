#printing the next character of the string
#s='abcdz' o/p:bcdea
s='abcdz'
s1=''
for c in s:
    if ord(c)>=97 and ord(c)<122:
        s1+=chr(ord(c)+1)
    else:
        s1+=chr(ord(c)-25)
print(s1)