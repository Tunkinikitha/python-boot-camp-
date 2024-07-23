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
      

