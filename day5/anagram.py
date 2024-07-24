#anagram
s1='tab'
s2='bat'
res1=sorted(s1)
res2=sorted(s2)
if len(s1)==len(s2) and res1==res2:
     print('anagram')
else:
     print('nothing')
