#arr=[1,1,0,1,1,0,0] o/p:0,0,0,1,1,1,1
arr=[1,1,0,1,1,0,0]
ones=[]
zeros=[]
for i in arr:
    if i==0:
        zeros.append(i)
    else:
        ones.append(i)
zeros.extend(ones)
print(zeros)