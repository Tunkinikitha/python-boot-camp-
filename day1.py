s='nikitha'
vowels=['a','e','i','o','u']
count=0
for c in s:
    if c in vowels:
        count+=1
print(count)        

#palindrome
s='python'
s1=''
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
    #print(s1)
if(s1==s):
    print('palindrome')
else:
    print('not')

