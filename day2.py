#list is collection of ordered elements mutable in nature
mobiles=['iphone','samsung','vivo']
mobiles.remove('samsung')
print(mobiles)

#pop() last element delete
mobiles=['iphone','samsung','vivo']
mobiles.pop()
print(mobiles)

#pop(0) index element ddelete
mobiles=['iphone','samsung','vivo']
mobiles.pop(0)
print(mobiles)

mobiles=['iphone','samsung','vivo']
mobiles.clear()
print(mobiles)

#update the list
mobiles=['iphone','samsung','vivo']
mobiles[1]='blackberry'
print(mobiles)

mobiles=['iphone','samsung','vivo','oppo','nothing']
print(mobiles[True])

mobiles=['iphone','samsung','vivo','oppo','nothing']
count=1
for ele in mobiles:
    print(count,ele)
    count+=1

#to print even
mobiles=['iphone','samsung','vivo','oppo','nothing']
for i in range(0,len(mobiles)):
    if i%2==0:
        print(mobiles[i])
#reverse
mobiles=['iphone','samsung','vivo','oppo','nothing']
for i in range(0,len(mobiles)):
    if i%2==0:
        rev=mobiles[i]
        print(rev[::-1])
    else:    
        print(mobiles[i])

#arr[1,2,3,4,5] k=4 o/p arr[4,5,1,2,3]
arr=[1,2,3,4,5]
k=4
first=arr[k-1:]
second=arr[:k-1]
print(first+second)

#or
arr=[1,2,3,4,5]
k=4
first=arr[k-1:]
second=arr[:k-1]
first.extend(second)
print(first)

#k=3 o/p[5,4,3,1,2]
arr=[1,2,3,4,5]
k=3
first=arr[k+1:k-(k-1):-1]
second=arr[:k-1]
print(first+second)

#k=2 #5,4,1,2,3 #wrong
arr=[1,2,3,4,5]
k=2
first=arr[k-1:]
first=first[::-1]
second=arr[:k+1]
print(first+second)

#tuples
#collection of mul data ele immutable
student=(101,'umer','cse','hyd')
#student.append('sridevi')#attributre error
print(student)

student=(101,'umer','cse','hyd')
student=list(student)
student[2]='ece'
print(student)

#dictionary
menu={'cb':555,'butter-chicken':450,
      'tandoori_chicken':555,
      'mandi':700}
menu['fruit_sald']=786
print(menu)

menu={'cb':555,'butter-chicken':450,
      'tandoori_chicken':555,
      'mandi':700}
menu.pop('cb')
print(menu)

# same key updated value we get
menu={'cb':555,'butter-chicken':450,
      'tandoori_chicken':555,
      'mandi':700,
      'mandi':999}
print(menu)

menu={'cb':555,'butter-chicken':450,
      'tandoori_chicken':555,
      'mandi':700}
for k,v in menu.items():
    print(k,'->',v)

#1,3,6,2,5,3,7,5,1 count the frequency of each number
arr=[1,3,6,2,5,3,7,5,1]
#1:2
#3:2
#6:1
#2:1
#5:2
#7:1
count=0
d={}
for key in arr:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
print(d)    
#unique elements
arr=[1,3,6,2,5,3,7,5,1]
#1:2
#3:2
#6:1
#2:1
#5:2
#7:1
count=0
d={}
for key in arr:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
print(d) 

#unique elements
arr=[1,3,6,2,5,3,7,5,1]
count=0
d={}
for key in arr:
    if key in d:
        d[key]=1
    else:
        d[key]=1
for num,count in d.items():
    if count==1:
        print(num)            

#max freq        
arr=[1,3,6,2,5,3,7,5,1]
count=0
d={}
for key in arr:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
for num,count in d.items():
    if count>1:
        print(num)   

#one town cong 7:5,18:22,32:8,71:5,66:6 ,bjp 17:15,18:20,32:4,71:9,66:2
cong={7:5,18:22,32:8,71:5,66:6}
bjp={7:15,18:20,32:4,71:9,66:2}
cong_sum=0
bjp_sum=0
for age,votes in cong.items():
    if age>=18:
        cong_sum+=votes
for age,votes in bjp.items():
    if age>=18:
        bjp_sum+=votes
diff=abs(cong_sum-bjp_sum)
if cong_sum>bjp_sum:
    print('cong win:',diff)
else:
    print('bjp win:',diff)
      

