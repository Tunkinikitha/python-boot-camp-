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