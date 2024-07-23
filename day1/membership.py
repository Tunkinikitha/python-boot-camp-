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