#count vowels in given string
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

#membership
s='123ABC$'
count=0
for i in s:
    if(not(i.isdigit())):
        count+=1
print(count)  

data=[1,8,'apple','carrot','mango']
fruits=['apple','mango','orange','watermelon']
vegies=['tomato','beans','carrot']
for i in data:
    if i not in fruits:
        print(i)

#identity
s='he is playing football but not cricket'
s=s.split()
print(len(s))

#count playing
s='he is playing football but he is not playing cricket'
s=s.split()
print(s.count('playing'))
print(s.count('he'))

#sum of digit when input is given
s=input()
sum=0
for i in range(0,len(s)):
    if s[i].isdigit():
        sum+=int(s[i])
print(sum)

#function
def greetings():
    return 'hello good morning'
print(greetings())

#
def greetings(branch):
    return'hello good mrng',branch
print(greetings('cse'))
print(greetings('it'))
print(greetings('ece'))


#even or odd
def check(n):
    if n%2==0:
        return"even"
    else:
        return"odd"
print(check(4))

#
def check(n):
    if 1&n==0:
        return"even"
    else:
        return"odd"
print(check(2))
#01
#10
#00

#count the no of elements div by 4 and 6
def check(arr):
    count=0 
    for i in arr:
        if i%4==0 and i%6==0:
            print(i,end=' ')
            count+=1
    return count
arr=[1,36,9,24,4,2,12] 
print('the count is :',check(arr))       


#rev of char
def check(s):
    rev=' '
    for i in s:
        rev=i+rev
    print(type(rev))    
    return rev
s='sridevi womens engineering college'
print(check(s))
    
#    
def check(s):
    s=s.split()
    s=list(reversed(s)) #s become reverse list
    print(s)
    for i in s:
        rev=i[::-1]
        print(rev,end=' ')
s='sridevi womens engineering college'
check(s)        

#fib
def check(n):
    first=0
    second=1
    print(first,second,end=' ')
    count=2
    while count<n:
        third=first+second
        print(third,end=' ')
        first=second
        second=third
        count+=
check(10)

#one fun calling another fun
def check(ele):
    return ele%2==0
def increment(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
    return count
arr=[5,9,12,6,17,3]
print(increment(arr))        

#palindrome
def check(ele):
    ele=str(ele)
    return ele==ele[::-1]
def increment(arr):
    count=0
    for ele in arr:
        if check(ele):
            print(ele)
            count+=1
    return count
arr=[21,78,212,782,1001]
print(increment(arr)) 

def check(n):
    n=str(n)
    return len(n)>1 and n==n[::-1]
def increment(N):
    count=0
    for i in range(1,N+1):
        if check(i):
            print(i)
            count+=1
    return count
N=50
print(increment(N))        


    
    
    



    