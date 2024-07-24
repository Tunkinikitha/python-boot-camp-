
#s=7,t=11,a=3,b=15
#apple=[6,5,-4],oranges=[9,8,-4]
s=7
t=11
a=3
b=15
apples=[6,5,-4]
oranges=[9,8,-4]
acount,ocount=0,0
for i in apples:
    if a+i in range(s,t+1):
        acount+=1
for i in oranges:
    if b+i in range(s,t+1):
        ocount+=1
print(acount,ocount)

#n=2397
#m=3 o/p:592721
#if even digit then add with m
#if odd digit then multiply with m
n=2397
m=3
n=str(n)
for i in n:
    if int(i)%2==0:
        print(int(i)+m,end='')
    else:
        print(int(i)+m,end='')

 #str'a1b2c3d492nm45'
 # o/p:12349245abcdnm 
str='a1b2c3d492nm45'
s1=''
s2=''
for c in str:
    if c.isdigit():
        s1+=c
    else:
        s2+=c
print(s1+s2)

# s='1c0c1c1a0b1'
#a &
#b |
#c ^
s='1c0c1c1a0b1'
res=int(s[0])
for i in range(1,len(s),2):
    if s[i]=='a':
        res=res&int(s[i+1])
    elif s[i]=='b':
        res=res|int(s[i+1])
    elif s[i]=='c':
         res=res^int(s[i+1])
print(res)

#s='apple' arrange characters in alphabetical order
#a->1,p->16,1->12,e->5
s='apple'
for c in s:
    print(c,'->',ord(c)-96)
