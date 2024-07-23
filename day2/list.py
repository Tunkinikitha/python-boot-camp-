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